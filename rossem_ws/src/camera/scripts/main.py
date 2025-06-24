#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped

import argparse
import os.path
import json
import cv2
import depthai as dai
import time

start_detection = False

def arduino_callback(msg):
    global start_detection
    if "motor" in msg.data.lower():
        print('jippie')
        rospy.loginfo("Startsignaal ontvangen van Arduino: Sensor 2 heeft gedetecteerd.")
        start_detection = True
    else: 
        print('stront aan de knikker')

def main():
    global start_detection

    parser = argparse.ArgumentParser()
    parser.add_argument('-j', type=str, required=True)
    parser.add_argument('-b', type=str, required=True)
    args, _ = parser.parse_known_args()
    blob_filename = args.b
    json_filename = args.j

    if not os.path.isfile(blob_filename) or not os.path.isfile(json_filename):
        rospy.logerr('Error: Bestanden niet gevonden')
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

    rospy.init_node('camera_detection_node', anonymous=True)

    error_pub = rospy.Publisher('/camera/error', String, queue_size=10)
    pose_pub = rospy.Publisher('/camera/detected_pose', PoseStamped, queue_size=10)
    label_pub = rospy.Publisher('/camera/detected_label', String, queue_size=10)

    rospy.Subscriber('/arduino/output', String, arduino_callback)

    rospy.loginfo("Wacht op start van Arduino...")
    rate = rospy.Rate(10)

    try:
        while not rospy.is_shutdown():
            if start_detection:
                rospy.loginfo("Start detectieproces...")

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
                        elif (time.time() - last_detection_time) > timeout_duration:
                            rospy.logwarn("Geen object gedetecteerd binnen 15 seconden!")
                            error_pub.publish("no_detection")
                            last_detection_time = time.time()

                        for detection in detections:
                            x1 = int(detection.xmin * frame.shape[1])
                            x2 = int(detection.xmax * frame.shape[1])
                            y1 = int(detection.ymin * frame.shape[0])
                            y2 = int(detection.ymax * frame.shape[0])

                            label = labelMap[detection.label] if detection.label < len(labelMap) else str(detection.label)
                            spatial_coords = detection.spatialCoordinates

                            pose_msg = PoseStamped()
                            pose_msg.header.stamp = rospy.Time.now()
                            pose_msg.header.frame_id = "oak_camera_frame"
                            pose_msg.pose.position.x = spatial_coords.x / 1000.0
                            pose_msg.pose.position.y = spatial_coords.y / 1000.0
                            pose_msg.pose.position.z = spatial_coords.z / 1000.0
                            pose_msg.pose.orientation.w = 1.0

                            pose_pub.publish(pose_msg)
                            label_pub.publish(label)

                            cv2.putText(frame, str(label), (x1 + 10, y1 + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
                            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)

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
        rospy.logerr(f"Camera-error: {e}")
        error_pub.publish("camera_error")


if __name__ == "__main__":
    main()
