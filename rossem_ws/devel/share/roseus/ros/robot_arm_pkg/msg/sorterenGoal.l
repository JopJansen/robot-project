;; Auto-generated. Do not edit!


(when (boundp 'robot_arm_pkg::sorterenGoal)
  (if (not (find-package "ROBOT_ARM_PKG"))
    (make-package "ROBOT_ARM_PKG"))
  (shadow 'sorterenGoal (find-package "ROBOT_ARM_PKG")))
(unless (find-package "ROBOT_ARM_PKG::SORTERENGOAL")
  (make-package "ROBOT_ARM_PKG::SORTERENGOAL"))

(in-package "ROS")
;;//! \htmlinclude sorterenGoal.msg.html


(defclass robot_arm_pkg::sorterenGoal
  :super ros::object
  :slots (_doel_positie ))

(defmethod robot_arm_pkg::sorterenGoal
  (:init
   (&key
    ((:doel_positie __doel_positie) "")
    )
   (send-super :init)
   (setq _doel_positie (string __doel_positie))
   self)
  (:doel_positie
   (&optional __doel_positie)
   (if __doel_positie (setq _doel_positie __doel_positie)) _doel_positie)
  (:serialization-length
   ()
   (+
    ;; string _doel_positie
    4 (length _doel_positie)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _doel_positie
       (write-long (length _doel_positie) s) (princ _doel_positie s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _doel_positie
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _doel_positie (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get robot_arm_pkg::sorterenGoal :md5sum-) "d0e6e9e8936cc5ed9f03d68751151301")
(setf (get robot_arm_pkg::sorterenGoal :datatype-) "robot_arm_pkg/sorterenGoal")
(setf (get robot_arm_pkg::sorterenGoal :definition-)
      "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
# Goal
string doel_positie


")



(provide :robot_arm_pkg/sorterenGoal "d0e6e9e8936cc5ed9f03d68751151301")


