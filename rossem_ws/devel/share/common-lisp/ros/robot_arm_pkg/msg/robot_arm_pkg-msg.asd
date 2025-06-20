
(cl:in-package :asdf)

(defsystem "robot_arm_pkg-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :actionlib_msgs-msg
               :std_msgs-msg
)
  :components ((:file "_package")
    (:file "sorterenAction" :depends-on ("_package_sorterenAction"))
    (:file "_package_sorterenAction" :depends-on ("_package"))
    (:file "sorterenActionFeedback" :depends-on ("_package_sorterenActionFeedback"))
    (:file "_package_sorterenActionFeedback" :depends-on ("_package"))
    (:file "sorterenActionGoal" :depends-on ("_package_sorterenActionGoal"))
    (:file "_package_sorterenActionGoal" :depends-on ("_package"))
    (:file "sorterenActionResult" :depends-on ("_package_sorterenActionResult"))
    (:file "_package_sorterenActionResult" :depends-on ("_package"))
    (:file "sorterenFeedback" :depends-on ("_package_sorterenFeedback"))
    (:file "_package_sorterenFeedback" :depends-on ("_package"))
    (:file "sorterenGoal" :depends-on ("_package_sorterenGoal"))
    (:file "_package_sorterenGoal" :depends-on ("_package"))
    (:file "sorterenResult" :depends-on ("_package_sorterenResult"))
    (:file "_package_sorterenResult" :depends-on ("_package"))
  ))