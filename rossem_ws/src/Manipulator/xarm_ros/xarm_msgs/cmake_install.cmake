# Install script for directory: /home/student/ufactory_ws/src/xarm_ros/xarm_msgs

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/student/ufactory_ws/install")
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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/xarm_msgs/msg" TYPE FILE FILES
    "/home/student/ufactory_ws/src/xarm_ros/xarm_msgs/msg/RobotMsg.msg"
    "/home/student/ufactory_ws/src/xarm_ros/xarm_msgs/msg/IOState.msg"
    "/home/student/ufactory_ws/src/xarm_ros/xarm_msgs/msg/CIOState.msg"
    "/home/student/ufactory_ws/src/xarm_ros/xarm_msgs/msg/VeloMoveMsg.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/xarm_msgs/srv" TYPE FILE FILES
    "/home/student/ufactory_ws/src/xarm_ros/xarm_msgs/srv/Move.srv"
    "/home/student/ufactory_ws/src/xarm_ros/xarm_msgs/srv/SetAxis.srv"
    "/home/student/ufactory_ws/src/xarm_ros/xarm_msgs/srv/SetInt16.srv"
    "/home/student/ufactory_ws/src/xarm_ros/xarm_msgs/srv/TCPOffset.srv"
    "/home/student/ufactory_ws/src/xarm_ros/xarm_msgs/srv/SetDigitalIO.srv"
    "/home/student/ufactory_ws/src/xarm_ros/xarm_msgs/srv/GetDigitalIO.srv"
    "/home/student/ufactory_ws/src/xarm_ros/xarm_msgs/srv/GetAnalogIO.srv"
    "/home/student/ufactory_ws/src/xarm_ros/xarm_msgs/srv/ClearErr.srv"
    "/home/student/ufactory_ws/src/xarm_ros/xarm_msgs/srv/GetErr.srv"
    "/home/student/ufactory_ws/src/xarm_ros/xarm_msgs/srv/GripperConfig.srv"
    "/home/student/ufactory_ws/src/xarm_ros/xarm_msgs/srv/GripperMove.srv"
    "/home/student/ufactory_ws/src/xarm_ros/xarm_msgs/srv/GripperState.srv"
    "/home/student/ufactory_ws/src/xarm_ros/xarm_msgs/srv/SetLoad.srv"
    "/home/student/ufactory_ws/src/xarm_ros/xarm_msgs/srv/SetToolModbus.srv"
    "/home/student/ufactory_ws/src/xarm_ros/xarm_msgs/srv/ConfigToolModbus.srv"
    "/home/student/ufactory_ws/src/xarm_ros/xarm_msgs/srv/GetControllerDigitalIO.srv"
    "/home/student/ufactory_ws/src/xarm_ros/xarm_msgs/srv/SetControllerAnalogIO.srv"
    "/home/student/ufactory_ws/src/xarm_ros/xarm_msgs/srv/MoveAxisAngle.srv"
    "/home/student/ufactory_ws/src/xarm_ros/xarm_msgs/srv/MoveVelo.srv"
    "/home/student/ufactory_ws/src/xarm_ros/xarm_msgs/srv/MoveVelocity.srv"
    "/home/student/ufactory_ws/src/xarm_ros/xarm_msgs/srv/SetFloat32.srv"
    "/home/student/ufactory_ws/src/xarm_ros/xarm_msgs/srv/SetMultipleInts.srv"
    "/home/student/ufactory_ws/src/xarm_ros/xarm_msgs/srv/SetString.srv"
    "/home/student/ufactory_ws/src/xarm_ros/xarm_msgs/srv/PlayTraj.srv"
    "/home/student/ufactory_ws/src/xarm_ros/xarm_msgs/srv/GetFloat32List.srv"
    "/home/student/ufactory_ws/src/xarm_ros/xarm_msgs/srv/GetInt32.srv"
    "/home/student/ufactory_ws/src/xarm_ros/xarm_msgs/srv/SetModbusTimeout.srv"
    "/home/student/ufactory_ws/src/xarm_ros/xarm_msgs/srv/GetSetModbusData.srv"
    "/home/student/ufactory_ws/src/xarm_ros/xarm_msgs/srv/Call.srv"
    "/home/student/ufactory_ws/src/xarm_ros/xarm_msgs/srv/FtCaliLoad.srv"
    "/home/student/ufactory_ws/src/xarm_ros/xarm_msgs/srv/FtIdenLoad.srv"
    "/home/student/ufactory_ws/src/xarm_ros/xarm_msgs/srv/VacuumGripperCtrl.srv"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/xarm_msgs/cmake" TYPE FILE FILES "/home/student/ufactory_ws/build/xarm_ros/xarm_msgs/catkin_generated/installspace/xarm_msgs-msg-paths.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/student/ufactory_ws/devel/include/xarm_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/student/ufactory_ws/devel/share/roseus/ros/xarm_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/student/ufactory_ws/devel/share/common-lisp/ros/xarm_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/student/ufactory_ws/devel/share/gennodejs/ros/xarm_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/usr/bin/python2" -m compileall "/home/student/ufactory_ws/devel/lib/python2.7/dist-packages/xarm_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/home/student/ufactory_ws/devel/lib/python2.7/dist-packages/xarm_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/student/ufactory_ws/build/xarm_ros/xarm_msgs/catkin_generated/installspace/xarm_msgs.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/xarm_msgs/cmake" TYPE FILE FILES "/home/student/ufactory_ws/build/xarm_ros/xarm_msgs/catkin_generated/installspace/xarm_msgs-msg-extras.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/xarm_msgs/cmake" TYPE FILE FILES
    "/home/student/ufactory_ws/build/xarm_ros/xarm_msgs/catkin_generated/installspace/xarm_msgsConfig.cmake"
    "/home/student/ufactory_ws/build/xarm_ros/xarm_msgs/catkin_generated/installspace/xarm_msgsConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/xarm_msgs" TYPE FILE FILES "/home/student/ufactory_ws/src/xarm_ros/xarm_msgs/package.xml")
endif()

