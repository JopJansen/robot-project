# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "robot_arm_pkg: 7 messages, 0 services")

set(MSG_I_FLAGS "-Irobot_arm_pkg:/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg;-Istd_msgs:/opt/ros/melodic/share/std_msgs/cmake/../msg;-Iactionlib_msgs:/opt/ros/melodic/share/actionlib_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(robot_arm_pkg_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenResult.msg" NAME_WE)
add_custom_target(_robot_arm_pkg_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "robot_arm_pkg" "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenResult.msg" ""
)

get_filename_component(_filename "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenAction.msg" NAME_WE)
add_custom_target(_robot_arm_pkg_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "robot_arm_pkg" "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenAction.msg" "actionlib_msgs/GoalID:actionlib_msgs/GoalStatus:robot_arm_pkg/SorterenResult:robot_arm_pkg/SorterenActionFeedback:robot_arm_pkg/SorterenActionResult:robot_arm_pkg/SorterenActionGoal:std_msgs/Header:robot_arm_pkg/SorterenGoal:robot_arm_pkg/SorterenFeedback"
)

get_filename_component(_filename "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenActionGoal.msg" NAME_WE)
add_custom_target(_robot_arm_pkg_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "robot_arm_pkg" "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenActionGoal.msg" "actionlib_msgs/GoalID:robot_arm_pkg/SorterenGoal:std_msgs/Header"
)

get_filename_component(_filename "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenFeedback.msg" NAME_WE)
add_custom_target(_robot_arm_pkg_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "robot_arm_pkg" "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenFeedback.msg" ""
)

get_filename_component(_filename "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenActionResult.msg" NAME_WE)
add_custom_target(_robot_arm_pkg_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "robot_arm_pkg" "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenActionResult.msg" "actionlib_msgs/GoalID:actionlib_msgs/GoalStatus:robot_arm_pkg/SorterenResult:std_msgs/Header"
)

get_filename_component(_filename "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenGoal.msg" NAME_WE)
add_custom_target(_robot_arm_pkg_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "robot_arm_pkg" "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenGoal.msg" ""
)

get_filename_component(_filename "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenActionFeedback.msg" NAME_WE)
add_custom_target(_robot_arm_pkg_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "robot_arm_pkg" "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenActionFeedback.msg" "actionlib_msgs/GoalID:actionlib_msgs/GoalStatus:robot_arm_pkg/SorterenFeedback:std_msgs/Header"
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(robot_arm_pkg
  "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/robot_arm_pkg
)
_generate_msg_cpp(robot_arm_pkg
  "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenAction.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenResult.msg;/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenActionFeedback.msg;/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenActionResult.msg;/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenActionGoal.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg;/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenGoal.msg;/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenFeedback.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/robot_arm_pkg
)
_generate_msg_cpp(robot_arm_pkg
  "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenGoal.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/robot_arm_pkg
)
_generate_msg_cpp(robot_arm_pkg
  "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/robot_arm_pkg
)
_generate_msg_cpp(robot_arm_pkg
  "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenActionResult.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenResult.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/robot_arm_pkg
)
_generate_msg_cpp(robot_arm_pkg
  "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenGoal.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/robot_arm_pkg
)
_generate_msg_cpp(robot_arm_pkg
  "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenFeedback.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/robot_arm_pkg
)

### Generating Services

### Generating Module File
_generate_module_cpp(robot_arm_pkg
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/robot_arm_pkg
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(robot_arm_pkg_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(robot_arm_pkg_generate_messages robot_arm_pkg_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenResult.msg" NAME_WE)
add_dependencies(robot_arm_pkg_generate_messages_cpp _robot_arm_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenAction.msg" NAME_WE)
add_dependencies(robot_arm_pkg_generate_messages_cpp _robot_arm_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenActionGoal.msg" NAME_WE)
add_dependencies(robot_arm_pkg_generate_messages_cpp _robot_arm_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenFeedback.msg" NAME_WE)
add_dependencies(robot_arm_pkg_generate_messages_cpp _robot_arm_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenActionResult.msg" NAME_WE)
add_dependencies(robot_arm_pkg_generate_messages_cpp _robot_arm_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenGoal.msg" NAME_WE)
add_dependencies(robot_arm_pkg_generate_messages_cpp _robot_arm_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenActionFeedback.msg" NAME_WE)
add_dependencies(robot_arm_pkg_generate_messages_cpp _robot_arm_pkg_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(robot_arm_pkg_gencpp)
add_dependencies(robot_arm_pkg_gencpp robot_arm_pkg_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS robot_arm_pkg_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(robot_arm_pkg
  "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/robot_arm_pkg
)
_generate_msg_eus(robot_arm_pkg
  "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenAction.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenResult.msg;/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenActionFeedback.msg;/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenActionResult.msg;/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenActionGoal.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg;/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenGoal.msg;/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenFeedback.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/robot_arm_pkg
)
_generate_msg_eus(robot_arm_pkg
  "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenGoal.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/robot_arm_pkg
)
_generate_msg_eus(robot_arm_pkg
  "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/robot_arm_pkg
)
_generate_msg_eus(robot_arm_pkg
  "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenActionResult.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenResult.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/robot_arm_pkg
)
_generate_msg_eus(robot_arm_pkg
  "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenGoal.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/robot_arm_pkg
)
_generate_msg_eus(robot_arm_pkg
  "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenFeedback.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/robot_arm_pkg
)

### Generating Services

### Generating Module File
_generate_module_eus(robot_arm_pkg
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/robot_arm_pkg
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(robot_arm_pkg_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(robot_arm_pkg_generate_messages robot_arm_pkg_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenResult.msg" NAME_WE)
add_dependencies(robot_arm_pkg_generate_messages_eus _robot_arm_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenAction.msg" NAME_WE)
add_dependencies(robot_arm_pkg_generate_messages_eus _robot_arm_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenActionGoal.msg" NAME_WE)
add_dependencies(robot_arm_pkg_generate_messages_eus _robot_arm_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenFeedback.msg" NAME_WE)
add_dependencies(robot_arm_pkg_generate_messages_eus _robot_arm_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenActionResult.msg" NAME_WE)
add_dependencies(robot_arm_pkg_generate_messages_eus _robot_arm_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenGoal.msg" NAME_WE)
add_dependencies(robot_arm_pkg_generate_messages_eus _robot_arm_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenActionFeedback.msg" NAME_WE)
add_dependencies(robot_arm_pkg_generate_messages_eus _robot_arm_pkg_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(robot_arm_pkg_geneus)
add_dependencies(robot_arm_pkg_geneus robot_arm_pkg_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS robot_arm_pkg_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(robot_arm_pkg
  "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/robot_arm_pkg
)
_generate_msg_lisp(robot_arm_pkg
  "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenAction.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenResult.msg;/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenActionFeedback.msg;/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenActionResult.msg;/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenActionGoal.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg;/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenGoal.msg;/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenFeedback.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/robot_arm_pkg
)
_generate_msg_lisp(robot_arm_pkg
  "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenGoal.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/robot_arm_pkg
)
_generate_msg_lisp(robot_arm_pkg
  "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/robot_arm_pkg
)
_generate_msg_lisp(robot_arm_pkg
  "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenActionResult.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenResult.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/robot_arm_pkg
)
_generate_msg_lisp(robot_arm_pkg
  "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenGoal.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/robot_arm_pkg
)
_generate_msg_lisp(robot_arm_pkg
  "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenFeedback.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/robot_arm_pkg
)

### Generating Services

### Generating Module File
_generate_module_lisp(robot_arm_pkg
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/robot_arm_pkg
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(robot_arm_pkg_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(robot_arm_pkg_generate_messages robot_arm_pkg_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenResult.msg" NAME_WE)
add_dependencies(robot_arm_pkg_generate_messages_lisp _robot_arm_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenAction.msg" NAME_WE)
add_dependencies(robot_arm_pkg_generate_messages_lisp _robot_arm_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenActionGoal.msg" NAME_WE)
add_dependencies(robot_arm_pkg_generate_messages_lisp _robot_arm_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenFeedback.msg" NAME_WE)
add_dependencies(robot_arm_pkg_generate_messages_lisp _robot_arm_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenActionResult.msg" NAME_WE)
add_dependencies(robot_arm_pkg_generate_messages_lisp _robot_arm_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenGoal.msg" NAME_WE)
add_dependencies(robot_arm_pkg_generate_messages_lisp _robot_arm_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenActionFeedback.msg" NAME_WE)
add_dependencies(robot_arm_pkg_generate_messages_lisp _robot_arm_pkg_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(robot_arm_pkg_genlisp)
add_dependencies(robot_arm_pkg_genlisp robot_arm_pkg_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS robot_arm_pkg_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(robot_arm_pkg
  "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/robot_arm_pkg
)
_generate_msg_nodejs(robot_arm_pkg
  "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenAction.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenResult.msg;/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenActionFeedback.msg;/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenActionResult.msg;/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenActionGoal.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg;/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenGoal.msg;/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenFeedback.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/robot_arm_pkg
)
_generate_msg_nodejs(robot_arm_pkg
  "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenGoal.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/robot_arm_pkg
)
_generate_msg_nodejs(robot_arm_pkg
  "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/robot_arm_pkg
)
_generate_msg_nodejs(robot_arm_pkg
  "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenActionResult.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenResult.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/robot_arm_pkg
)
_generate_msg_nodejs(robot_arm_pkg
  "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenGoal.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/robot_arm_pkg
)
_generate_msg_nodejs(robot_arm_pkg
  "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenFeedback.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/robot_arm_pkg
)

### Generating Services

### Generating Module File
_generate_module_nodejs(robot_arm_pkg
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/robot_arm_pkg
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(robot_arm_pkg_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(robot_arm_pkg_generate_messages robot_arm_pkg_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenResult.msg" NAME_WE)
add_dependencies(robot_arm_pkg_generate_messages_nodejs _robot_arm_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenAction.msg" NAME_WE)
add_dependencies(robot_arm_pkg_generate_messages_nodejs _robot_arm_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenActionGoal.msg" NAME_WE)
add_dependencies(robot_arm_pkg_generate_messages_nodejs _robot_arm_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenFeedback.msg" NAME_WE)
add_dependencies(robot_arm_pkg_generate_messages_nodejs _robot_arm_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenActionResult.msg" NAME_WE)
add_dependencies(robot_arm_pkg_generate_messages_nodejs _robot_arm_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenGoal.msg" NAME_WE)
add_dependencies(robot_arm_pkg_generate_messages_nodejs _robot_arm_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenActionFeedback.msg" NAME_WE)
add_dependencies(robot_arm_pkg_generate_messages_nodejs _robot_arm_pkg_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(robot_arm_pkg_gennodejs)
add_dependencies(robot_arm_pkg_gennodejs robot_arm_pkg_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS robot_arm_pkg_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(robot_arm_pkg
  "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/robot_arm_pkg
)
_generate_msg_py(robot_arm_pkg
  "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenAction.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenResult.msg;/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenActionFeedback.msg;/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenActionResult.msg;/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenActionGoal.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg;/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenGoal.msg;/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenFeedback.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/robot_arm_pkg
)
_generate_msg_py(robot_arm_pkg
  "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenGoal.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/robot_arm_pkg
)
_generate_msg_py(robot_arm_pkg
  "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/robot_arm_pkg
)
_generate_msg_py(robot_arm_pkg
  "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenActionResult.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenResult.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/robot_arm_pkg
)
_generate_msg_py(robot_arm_pkg
  "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenGoal.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/robot_arm_pkg
)
_generate_msg_py(robot_arm_pkg
  "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenFeedback.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/robot_arm_pkg
)

### Generating Services

### Generating Module File
_generate_module_py(robot_arm_pkg
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/robot_arm_pkg
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(robot_arm_pkg_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(robot_arm_pkg_generate_messages robot_arm_pkg_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenResult.msg" NAME_WE)
add_dependencies(robot_arm_pkg_generate_messages_py _robot_arm_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenAction.msg" NAME_WE)
add_dependencies(robot_arm_pkg_generate_messages_py _robot_arm_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenActionGoal.msg" NAME_WE)
add_dependencies(robot_arm_pkg_generate_messages_py _robot_arm_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenFeedback.msg" NAME_WE)
add_dependencies(robot_arm_pkg_generate_messages_py _robot_arm_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenActionResult.msg" NAME_WE)
add_dependencies(robot_arm_pkg_generate_messages_py _robot_arm_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenGoal.msg" NAME_WE)
add_dependencies(robot_arm_pkg_generate_messages_py _robot_arm_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/student/Git-projects/robot-project/rossem_ws/devel/share/robot_arm_pkg/msg/SorterenActionFeedback.msg" NAME_WE)
add_dependencies(robot_arm_pkg_generate_messages_py _robot_arm_pkg_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(robot_arm_pkg_genpy)
add_dependencies(robot_arm_pkg_genpy robot_arm_pkg_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS robot_arm_pkg_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/robot_arm_pkg)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/robot_arm_pkg
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(robot_arm_pkg_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()
if(TARGET actionlib_msgs_generate_messages_cpp)
  add_dependencies(robot_arm_pkg_generate_messages_cpp actionlib_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/robot_arm_pkg)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/robot_arm_pkg
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(robot_arm_pkg_generate_messages_eus std_msgs_generate_messages_eus)
endif()
if(TARGET actionlib_msgs_generate_messages_eus)
  add_dependencies(robot_arm_pkg_generate_messages_eus actionlib_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/robot_arm_pkg)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/robot_arm_pkg
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(robot_arm_pkg_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()
if(TARGET actionlib_msgs_generate_messages_lisp)
  add_dependencies(robot_arm_pkg_generate_messages_lisp actionlib_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/robot_arm_pkg)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/robot_arm_pkg
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(robot_arm_pkg_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()
if(TARGET actionlib_msgs_generate_messages_nodejs)
  add_dependencies(robot_arm_pkg_generate_messages_nodejs actionlib_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/robot_arm_pkg)
  install(CODE "execute_process(COMMAND \"/usr/bin/python2\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/robot_arm_pkg\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/robot_arm_pkg
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(robot_arm_pkg_generate_messages_py std_msgs_generate_messages_py)
endif()
if(TARGET actionlib_msgs_generate_messages_py)
  add_dependencies(robot_arm_pkg_generate_messages_py actionlib_msgs_generate_messages_py)
endif()
