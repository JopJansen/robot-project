# Install script for directory: /home/student/Git-projects/robot-project/rossem_ws/src/Manipulator/xarm_ros/xarm_gripper

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/student/Git-projects/robot-project/rossem_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/xarm_gripper/action" TYPE FILE FILES "/home/student/Git-projects/robot-project/rossem_ws/src/Manipulator/xarm_ros/xarm_gripper/action/Move.action")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/xarm_gripper/msg" TYPE FILE FILES
    "/home/student/Git-projects/robot-project/rossem_ws/devel/share/xarm_gripper/msg/MoveAction.msg"
    "/home/student/Git-projects/robot-project/rossem_ws/devel/share/xarm_gripper/msg/MoveActionGoal.msg"
    "/home/student/Git-projects/robot-project/rossem_ws/devel/share/xarm_gripper/msg/MoveActionResult.msg"
    "/home/student/Git-projects/robot-project/rossem_ws/devel/share/xarm_gripper/msg/MoveActionFeedback.msg"
    "/home/student/Git-projects/robot-project/rossem_ws/devel/share/xarm_gripper/msg/MoveGoal.msg"
    "/home/student/Git-projects/robot-project/rossem_ws/devel/share/xarm_gripper/msg/MoveResult.msg"
    "/home/student/Git-projects/robot-project/rossem_ws/devel/share/xarm_gripper/msg/MoveFeedback.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/xarm_gripper/cmake" TYPE FILE FILES "/home/student/Git-projects/robot-project/rossem_ws/build/Manipulator/xarm_ros/xarm_gripper/catkin_generated/installspace/xarm_gripper-msg-paths.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/student/Git-projects/robot-project/rossem_ws/devel/include/xarm_gripper")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/student/Git-projects/robot-project/rossem_ws/devel/share/roseus/ros/xarm_gripper")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/student/Git-projects/robot-project/rossem_ws/devel/share/common-lisp/ros/xarm_gripper")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/student/Git-projects/robot-project/rossem_ws/devel/share/gennodejs/ros/xarm_gripper")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/usr/bin/python2" -m compileall "/home/student/Git-projects/robot-project/rossem_ws/devel/lib/python2.7/dist-packages/xarm_gripper")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/home/student/Git-projects/robot-project/rossem_ws/devel/lib/python2.7/dist-packages/xarm_gripper")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/student/Git-projects/robot-project/rossem_ws/build/Manipulator/xarm_ros/xarm_gripper/catkin_generated/installspace/xarm_gripper.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/xarm_gripper/cmake" TYPE FILE FILES "/home/student/Git-projects/robot-project/rossem_ws/build/Manipulator/xarm_ros/xarm_gripper/catkin_generated/installspace/xarm_gripper-msg-extras.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/xarm_gripper/cmake" TYPE FILE FILES
    "/home/student/Git-projects/robot-project/rossem_ws/build/Manipulator/xarm_ros/xarm_gripper/catkin_generated/installspace/xarm_gripperConfig.cmake"
    "/home/student/Git-projects/robot-project/rossem_ws/build/Manipulator/xarm_ros/xarm_gripper/catkin_generated/installspace/xarm_gripperConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/xarm_gripper" TYPE FILE FILES "/home/student/Git-projects/robot-project/rossem_ws/src/Manipulator/xarm_ros/xarm_gripper/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/xarm_gripper/config" TYPE DIRECTORY FILES "/home/student/Git-projects/robot-project/rossem_ws/src/Manipulator/xarm_ros/xarm_gripper/config/")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/xarm_gripper/launch" TYPE DIRECTORY FILES "/home/student/Git-projects/robot-project/rossem_ws/src/Manipulator/xarm_ros/xarm_gripper/launch/")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/xarm_gripper/meshes" TYPE DIRECTORY FILES "/home/student/Git-projects/robot-project/rossem_ws/src/Manipulator/xarm_ros/xarm_gripper/meshes/")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/xarm_gripper/urdf" TYPE DIRECTORY FILES "/home/student/Git-projects/robot-project/rossem_ws/src/Manipulator/xarm_ros/xarm_gripper/urdf/")
endif()

