# Install script for directory: /home/student/Git-projects/robot-project/rossem_ws/src/Manipulator/xarm_ros/examples/xarm7_redundancy_res

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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/student/Git-projects/robot-project/rossem_ws/build/Manipulator/xarm_ros/examples/xarm7_redundancy_res/catkin_generated/installspace/xarm7_redundancy_res.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/xarm7_redundancy_res/cmake" TYPE FILE FILES
    "/home/student/Git-projects/robot-project/rossem_ws/build/Manipulator/xarm_ros/examples/xarm7_redundancy_res/catkin_generated/installspace/xarm7_redundancy_resConfig.cmake"
    "/home/student/Git-projects/robot-project/rossem_ws/build/Manipulator/xarm_ros/examples/xarm7_redundancy_res/catkin_generated/installspace/xarm7_redundancy_resConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/xarm7_redundancy_res" TYPE FILE FILES "/home/student/Git-projects/robot-project/rossem_ws/src/Manipulator/xarm_ros/examples/xarm7_redundancy_res/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/xarm7_redundancy_res" TYPE PROGRAM FILES "/home/student/Git-projects/robot-project/rossem_ws/build/Manipulator/xarm_ros/examples/xarm7_redundancy_res/catkin_generated/installspace/robot_jogging.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/xarm7_redundancy_res" TYPE PROGRAM FILES "/home/student/Git-projects/robot-project/rossem_ws/build/Manipulator/xarm_ros/examples/xarm7_redundancy_res/catkin_generated/installspace/test.py")
endif()

