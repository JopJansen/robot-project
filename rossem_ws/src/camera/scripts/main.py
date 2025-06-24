def main():
    global start_detection

    parser = argparse.ArgumentParser()
    parser.add_argument('-j', type=str, required=True)
    parser.add_argument('-b', type=str, required=True)
    args, _ = parser.parse_known_args()
    blob_filename = args.b
    json_filename = args.j

    if (not os.path.isfile(blob_filename)) or (not os.path.isfile(json_filename)):
        rospy.logerr('Error: Bestanden niet gevonden')
        return

    with open(json_filename) as f:
        jsonData = json.load(f)

    # ... (alle instellingen en pipeline zoals in jouw code) ...

    rospy.init_node('camera_detection_node', anonymous=True)

    error_pub = rospy.Publisher('/camera/error', String, queue_size=10)
    pose_pub = rospy.Publisher('/camera/detected_pose', PoseStamped, queue_size=10)
    label_pub = rospy.Publisher('/camera/detected_label', String, queue_size=10)

    rospy.Subscriber('/arduino/output', String, arduino_callback)

    rospy.loginfo("Wacht op signaal van Arduino (sensor 2)...")
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
                    timeout_duration = 15

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
