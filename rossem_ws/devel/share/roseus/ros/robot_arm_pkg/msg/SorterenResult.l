;; Auto-generated. Do not edit!


(when (boundp 'robot_arm_pkg::SorterenResult)
  (if (not (find-package "ROBOT_ARM_PKG"))
    (make-package "ROBOT_ARM_PKG"))
  (shadow 'SorterenResult (find-package "ROBOT_ARM_PKG")))
(unless (find-package "ROBOT_ARM_PKG::SORTERENRESULT")
  (make-package "ROBOT_ARM_PKG::SORTERENRESULT"))

(in-package "ROS")
;;//! \htmlinclude SorterenResult.msg.html


(defclass robot_arm_pkg::SorterenResult
  :super ros::object
  :slots (_success ))

(defmethod robot_arm_pkg::SorterenResult
  (:init
   (&key
    ((:success __success) nil)
    )
   (send-super :init)
   (setq _success __success)
   self)
  (:success
   (&optional __success)
   (if __success (setq _success __success)) _success)
  (:serialization-length
   ()
   (+
    ;; bool _success
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _success
       (if _success (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _success
     (setq _success (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(setf (get robot_arm_pkg::SorterenResult :md5sum-) "358e233cde0c8a8bcfea4ce193f8fc15")
(setf (get robot_arm_pkg::SorterenResult :datatype-) "robot_arm_pkg/SorterenResult")
(setf (get robot_arm_pkg::SorterenResult :definition-)
      "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
# Result
bool success


")



(provide :robot_arm_pkg/SorterenResult "358e233cde0c8a8bcfea4ce193f8fc15")


