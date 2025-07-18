# Install script for directory: /home/student/Git-projects/robot-project/rossem_ws/src/Manipulator/xarm_ros/xarm_vision/d435i_xarm_setup

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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/student/Git-projects/robot-project/rossem_ws/build/Manipulator/xarm_ros/xarm_vision/d435i_xarm_setup/catkin_generated/installspace/d435i_xarm_setup.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/d435i_xarm_setup/cmake" TYPE FILE FILES
    "/home/student/Git-projects/robot-project/rossem_ws/build/Manipulator/xarm_ros/xarm_vision/d435i_xarm_setup/catkin_generated/installspace/d435i_xarm_setupConfig.cmake"
    "/home/student/Git-projects/robot-project/rossem_ws/build/Manipulator/xarm_ros/xarm_vision/d435i_xarm_setup/catkin_generated/installspace/d435i_xarm_setupConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/d435i_xarm_setup" TYPE FILE FILES "/home/student/Git-projects/robot-project/rossem_ws/src/Manipulator/xarm_ros/xarm_vision/d435i_xarm_setup/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/d435i_xarm_setup" TYPE DIRECTORY FILES "/home/student/Git-projects/robot-project/rossem_ws/src/Manipulator/xarm_ros/xarm_vision/d435i_xarm_setup/launch")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/d435i_xarm_setup/findobj2d_grasp_api" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/d435i_xarm_setup/findobj2d_grasp_api")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/d435i_xarm_setup/findobj2d_grasp_api"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/d435i_xarm_setup" TYPE EXECUTABLE FILES "/home/student/Git-projects/robot-project/rossem_ws/devel/lib/d435i_xarm_setup/findobj2d_grasp_api")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/d435i_xarm_setup/findobj2d_grasp_api" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/d435i_xarm_setup/findobj2d_grasp_api")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/d435i_xarm_setup/findobj2d_grasp_api"
         OLD_RPATH "/opt/ros/melodic/lib:/home/student/Git-projects/robot-project/rossem_ws/devel/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/d435i_xarm_setup/findobj2d_grasp_api")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/d435i_xarm_setup/findobj2d_grasp_moveit" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/d435i_xarm_setup/findobj2d_grasp_moveit")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/d435i_xarm_setup/findobj2d_grasp_moveit"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/d435i_xarm_setup" TYPE EXECUTABLE FILES "/home/student/Git-projects/robot-project/rossem_ws/devel/lib/d435i_xarm_setup/findobj2d_grasp_moveit")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/d435i_xarm_setup/findobj2d_grasp_moveit" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/d435i_xarm_setup/findobj2d_grasp_moveit")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/d435i_xarm_setup/findobj2d_grasp_moveit"
         OLD_RPATH "/opt/ros/melodic/lib:/home/student/Git-projects/robot-project/rossem_ws/devel/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/d435i_xarm_setup/findobj2d_grasp_moveit")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/d435i_xarm_setup/obj2base" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/d435i_xarm_setup/obj2base")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/d435i_xarm_setup/obj2base"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/d435i_xarm_setup" TYPE EXECUTABLE FILES "/home/student/Git-projects/robot-project/rossem_ws/devel/lib/d435i_xarm_setup/obj2base")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/d435i_xarm_setup/obj2base" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/d435i_xarm_setup/obj2base")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/d435i_xarm_setup/obj2base"
         OLD_RPATH "/opt/ros/melodic/lib:/home/student/Git-projects/robot-project/rossem_ws/devel/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/d435i_xarm_setup/obj2base")
    endif()
  endif()
endif()

