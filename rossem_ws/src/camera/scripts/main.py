#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped
import argparse
import os.path
import json
import cv2
import depthai as dai
import time
import numpy as np
from scipy.spatial.transform import Rotation as R

start_detection = False
robot_start_sent = False
robot_start_pub = None

def arduino_callback(msg):
    global start_detection
    if "ready" in msg.data.lower():
        rospy.loginfo("Startsignaal ontvangen van Arduino: Sensor 2 heeft gedetecteerd.")
        start_detection = True
    else:
        rospy.logwarn("Onverwacht Arduino-signaal ontvangen: '%s'", msg.data)

def main():
    global start_detection
    global robot_start_sent
    global robot_start_pub

    parser = argparse.ArgumentParser()
    parser.add_argument('-j', type=str, required=True)
    parser.add_argument('-b', type=str, required=True)
    args, _ = parser.parse_known_args()
    blob_filename = args.b
    json_filename = args.j

    if not os.path.isfile(blob_filename) or not os.path.isfile(json_filename):
        print('Error: Bestanden niet gevonden')
        return

    with open(json_filename) as f:
        jsonData = json.load(f)

    numClasses = jsonData["nn_config"]["NN_specific_metadata"]["classes"]
    labelMap = jsonData["mappings"]["labels"]
    anchors = jsonData["nn_config"]["NN_specific_metadata"]["anchors"]
    anchorMasks = jsonData["nn_config"]["NN_specific_metadata"]["anchor_masks"]
    coordinateSize = jsonData["nn_config"]["NN_specific_metadata"]["coordinates"]
    iouThreshold = jsonData["nn_config"]["NN_specific_metadata"]["iou_threshold"]
    confidenceThreshold = jsonData["nn_config"]["NN_specific_metadata"]["confidence_threshold"]
    inputSizeX, inputSizeY = map(int, jsonData["nn_config"]["input_size"].split("x"))

    syncNN = True

    rospy.init_node('camera_detection_node', anonymous=True)
    rospy.Subscriber('/transportband/status', String, arduino_callback)

    error_pub = rospy.Publisher('/camera/error', String, queue_size=10)
    pose_pub = rospy.Publisher('/camera/detected_pose', PoseStamped, queue_size=10)
    label_pub = rospy.Publisher('/camera/detected_label', String, queue_size=10)
    camera_status_pub = rospy.Publisher('/camera/status', String, queue_size=10)

    rate = rospy.Rate(10)
    rospy.loginfo("Wacht op startsignaal van Arduino...")

    try:
        while not rospy.is_shutdown():
            if start_detection:
                rospy.loginfo("Start detectieproces...")

                pipeline = dai.Pipeline()

                camRgb = pipeline.create(dai.node.ColorCamera)
                spatialDetectionNetwork = pipeline.create(dai.node.YoloSpatialDetectionNetwork)
                monoLeft = pipeline.create(dai.node.MonoCamera)
                monoRight = pipeline.create(dai.node.MonoCamera)
                stereo = pipeline.create(dai.node.StereoDepth)

                xoutRgb = pipeline.create(dai.node.XLinkOut)
                xoutNN = pipeline.create(dai.node.XLinkOut)
                xoutDepth = pipeline.create(dai.node.XLinkOut)

                xoutRgb.setStreamName("rgb")
                xoutNN.setStreamName("detections")
                xoutDepth.setStreamName("depth")

                camRgb.setPreviewSize(inputSizeX, inputSizeY)
                camRgb.setResolution(dai.ColorCameraProperties.SensorResolution.THE_1080_P)
                camRgb.setInterleaved(False)
                camRgb.setColorOrder(dai.ColorCameraProperties.ColorOrder.BGR)

                monoLeft.setResolution(dai.MonoCameraProperties.SensorResolution.THE_400_P)
                monoLeft.setBoardSocket(dai.CameraBoardSocket.LEFT)
                monoRight.setResolution(dai.MonoCameraProperties.SensorResolution.THE_400_P)
                monoRight.setBoardSocket(dai.CameraBoardSocket.RIGHT)

                stereo.setDefaultProfilePreset(dai.node.StereoDepth.PresetMode.HIGH_DENSITY)
                stereo.setDepthAlign(dai.CameraBoardSocket.RGB)
                stereo.setOutputSize(monoLeft.getResolutionWidth(), monoLeft.getResolutionHeight())

                spatialDetectionNetwork.setBlobPath(blob_filename)
                spatialDetectionNetwork.setConfidenceThreshold(confidenceThreshold)
                spatialDetectionNetwork.input.setBlocking(False)
                spatialDetectionNetwork.setBoundingBoxScaleFactor(0.5)
                spatialDetectionNetwork.setDepthLowerThreshold(100)
                spatialDetectionNetwork.setDepthUpperThreshold(5000)
                spatialDetectionNetwork.setNumClasses(numClasses)
                spatialDetectionNetwork.setCoordinateSize(coordinateSize)
                spatialDetectionNetwork.setAnchors(anchors)
                spatialDetectionNetwork.setAnchorMasks(anchorMasks)
                spatialDetectionNetwork.setIouThreshold(iouThreshold)

                monoLeft.out.link(stereo.left)
                monoRight.out.link(stereo.right)
                camRgb.preview.link(spatialDetectionNetwork.input)
                spatialDetectionNetwork.out.link(xoutNN.input)
                stereo.depth.link(spatialDetectionNetwork.inputDepth)

                if syncNN:
                    spatialDetectionNetwork.passthrough.link(xoutRgb.input)
                    spatialDetectionNetwork.passthroughDepth.link(xoutDepth.input)
                else:
                    camRgb.preview.link(xoutRgb.input)

                with dai.Device(pipeline) as device:
                    previewQueue = device.getOutputQueue(name="rgb", maxSize=4, blocking=False)
                    detectionNNQueue = device.getOutputQueue(name="detections", maxSize=4, blocking=False)
                    depthQueue = device.getOutputQueue(name="depth", maxSize=4, blocking=False)

                    startTime = time.monotonic()
                    counter = 0
                    fps = 0
                    color = (255, 255, 255)
                    last_detection_time = time.time()
                    timeout_duration = 5
                    error_sent = False

                    while not rospy.is_shutdown() and start_detection:
                        inPreview = previewQueue.tryGet()
                        inDet = detectionNNQueue.tryGet()
                        depth = depthQueue.tryGet()

                        if inPreview is None or inDet is None or depth is None:
                            time.sleep(0.01)
                            continue

                        frame = inPreview.getCvFrame()
                        depthFrame = depth.getFrame()

                        counter += 1
                        current_time = time.monotonic()
                        if (current_time - startTime) > 1:
                            fps = counter / (current_time - startTime)
                            counter = 0
                            startTime = current_time

                        detections = inDet.detections

                        if detections:
                            last_detection_time = time.time()
                            error_sent = False
                        elif (time.time() - last_detection_time) > timeout_duration and not error_sent:
                            rospy.logwarn("Geen object gedetecteerd binnen 5 seconden!")
                            error_pub.publish("no_detection")
                            label_pub.publish("ERROR")
                            error_sent = True
                            last_detection_time = time.time()

                        for detection in detections:
                            x1 = int(detection.xmin * frame.shape[1])
                            x2 = int(detection.xmax * frame.shape[1])
                            y1 = int(detection.ymin * frame.shape[0])
                            y2 = int(detection.ymax * frame.shape[0])

                            x1 = max(0, x1)
                            y1 = max(0, y1)
                            x2 = min(frame.shape[1] - 1, x2)
                            y2 = min(frame.shape[0] - 1, y2)

                            if x2 <= x1 or y2 <= y1:
                                rospy.logwarn("Ongeldige bounding box, overslaan")
                                continue

                            roi = frame[y1:y2, x1:x2]
                            if roi.size == 0:
                                rospy.logwarn("ROI is leeg, overslaan")
                                continue

                            gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
                            _, thresh = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
                            contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

                            angle = 0.0
                            if contours:
                                c = max(contours, key=cv2.contourArea)
                                rect = cv2.minAreaRect(c)
                                angle = rect[2]
                                if rect[1][0] < rect[1][1]:
                                    angle += 90.0

                            quat = R.from_euler('z', angle, degrees=True).as_quat()

                            pose_msg = PoseStamped()
                            pose_msg.header.stamp = rospy.Time.now()
                            pose_msg.header.frame_id = "oak_camera_rgb_camera_optical_frame"
                            pose_msg.pose.position.x = detection.spatialCoordinates.x / 1000.0
                            pose_msg.pose.position.y = detection.spatialCoordinates.y / 1000.0
                            pose_msg.pose.position.z = 0.355
                            pose_msg.pose.orientation.x = quat[0]
                            pose_msg.pose.orientation.y = quat[1]
                            pose_msg.pose.orientation.z = quat[2]
                            pose_msg.pose.orientation.w = quat[3]

                            pose_pub.publish(pose_msg)
                            label = labelMap[detection.label] if detection.label < len(labelMap) else str(detection.label)
                            label_pub.publish(label)

                            if not robot_start_sent:
                                camera_status_pub.publish("klaar")
                                rospy.loginfo("Eerste coördinaat gepubliceerd -> START signaal naar /robot_start verstuurd")
                                robot_start_sent = True
                                start_detection = False
                                robot_start_sent = False
                                rospy.loginfo("Detectie afgerond, wacht opnieuw op nieuwe startsignaal...")
                                break

                        cv2.putText(frame, "FPS: {:.2f}".format(fps), (2, frame.shape[0] - 4), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
                        cv2.imshow("Detected objects", frame)

                        if cv2.waitKey(1) & 0xFF == ord('q'):
                            rospy.loginfo("Stoppen op 'q' toets.")
                            start_detection = False
                            break

                    cv2.destroyAllWindows()
            else:
                rate.sleep()

    except Exception as e:
        rospy.logerr("Camera-error: {}".format(e))
        error_pub.publish("camera_error")
        label_pub.publish("ERROR")

if __name__ == "__main__":
    main()