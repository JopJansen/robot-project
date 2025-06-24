#!/usr/bin/env python3

# === ROS AANPASSINGEN START ===
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped
# === ROS AANPASSINGEN EINDE ===

import argparse
import os.path
import json
import sys
import cv2
import depthai as dai
import numpy as np
import time

# === AANPASSINGEN VOOR STARTCONDITIE ===
start_detection = False

def arduino_callback(msg):
    global start_detection
    if "motor" in msg.data.lower():
        rospy.loginfo("Startsignaal ontvangen van Arduino: Sensor 2 heeft gedetecteerd.")
        start_detection = True
# === EINDE AANPASSINGEN ===

def main():
    global start_detection

    # Create the parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-j', type=str, required=True)
    parser.add_argument('-b', type=str, required=True)
    args = parser.parse_args()
    blob_filename = args.b
    json_filename = args.j

    if(not os.path.isfile(blob_filename)) or (not os.path.isfile(json_filename)):
        print('Error: Bestanden niet gevonden')
        return

    f = open(json_filename)
    jsonData = json.load(f)
    f.close()

    numClasses = jsonData["nn_config"]["NN_specific_metadata"]["classes"]
    labelMap = jsonData["mappings"]["labels"]
    anchors = jsonData["nn_config"]["NN_specific_metadata"]["anchors"]
    anchorMasks = jsonData["nn_config"]["NN_specific_metadata"]["anchor_masks"]
    coordinateSize = jsonData["nn_config"]["NN_specific_metadata"]["coordinates"]
    iouThreshold = jsonData["nn_config"]["NN_specific_metadata"]["iou_threshold"]
    confidenceThreshold = jsonData["nn_config"]["NN_specific_metadata"]["confidence_threshold"]
    inputSizeX, inputSizeY = map(int, jsonData["nn_config"]["input_size"].split("x"))

    syncNN = True

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

    # === ROS AANPASSINGEN START ===
    rospy.init_node('camera_detection_node', anonymous=True)

    # === publishers ===
    error_pub = rospy.Publisher('/camera/error', String, queue_size=10)
    pose_pub = rospy.Publisher('/camera/detected_pose', PoseStamped, queue_size=10)
    label_pub = rospy.Publisher('/camera/detected_label', String, queue_size=10)

    # === subscriber voor startconditie ===
    rospy.Subscriber('/arduino/output', String, arduino_callback)

    # Wacht tot startconditie
    rospy.loginfo("Wacht op signaal van Arduino (sensor 2)...")
    rate = rospy.Rate(10)
    while not rospy.is_shutdown() and not start_detection:
        rate.sleep()
    # === ROS AANPASSINGEN EINDE ===

    try:
        with dai.Device(pipeline) as device:
            previewQueue = device.getOutputQueue(name="rgb", maxSize=4, blocking=False)
            detectionNNQueue = device.getOutputQueue(name="detections", maxSize=4, blocking=False)
            depthQueue = device.getOutputQueue(name="depth", maxSize=4, blocking=False)

            startTime = time.monotonic()
            counter = 0
            fps = 0
            color = (255, 255, 255)

            last_detection_time = time.time()
            timeout_duration = 15  # seconden

            while not rospy.is_shutdown():
                inPreview = previewQueue.get()
                inDet = detectionNNQueue.get()
                depth = depthQueue.get()

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
                else:
                    if (time.time() - last_detection_time) > timeout_duration:
                        rospy.logwarn("Geen object gedetecteerd binnen 15 seconden!")
                        error_pub.publish("no_detection")
                        last_detection_time = time.time()

                for detection in detections:
                    x1 = int(detection.xmin * frame.shape[1])
                    x2 = int(detection.xmax * frame.shape[1])
                    y1 = int(detection.ymin * frame.shape[0])
                    y2 = int(detection.ymax * frame.shape[0])

                    try:
                        label = labelMap[detection.label]
                    except:
                        label = str(detection.label)

                    spatial_coords = detection.spatialCoordinates

                    pose_msg = PoseStamped()
                    pose_msg.header.stamp = rospy.Time.now()
                    pose_msg.header.frame_id = "camera_link"
                    pose_msg.pose.position.x = spatial_coords.x / 1000.0
                    pose_msg.pose.position.y = spatial_coords.y / 1000.0
                    pose_msg.pose.position.z = spatial_coords.z / 1000.0
                    pose_msg.pose.orientation.w = 1.0

                    pose_pub.publish(pose_msg)
                    label_pub.publish(label)

                    cv2.putText(frame, str(label), (x1 + 10, y1 + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, 255)
                    cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)

                cv2.putText(frame, "FPS: {:.2f}".format(fps), (2, frame.shape[0] - 4), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color)
                cv2.imshow("Detected objects", frame)

                if cv2.waitKey(1) == ord('q'):
                    break

    except Exception as e:
        rospy.logerr(f"Camera-error: {e}")
        error_pub.publish("camera_error")

if __name__ == "__main__":
    main()
