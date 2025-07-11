// Generated by gencpp from file xarm_msgs/MoveAxisAngleRequest.msg
// DO NOT EDIT!


#ifndef XARM_MSGS_MESSAGE_MOVEAXISANGLEREQUEST_H
#define XARM_MSGS_MESSAGE_MOVEAXISANGLEREQUEST_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace xarm_msgs
{
template <class ContainerAllocator>
struct MoveAxisAngleRequest_
{
  typedef MoveAxisAngleRequest_<ContainerAllocator> Type;

  MoveAxisAngleRequest_()
    : pose()
    , mvvelo(0.0)
    , mvacc(0.0)
    , mvtime(0.0)
    , coord(0)
    , relative(0)  {
    }
  MoveAxisAngleRequest_(const ContainerAllocator& _alloc)
    : pose(_alloc)
    , mvvelo(0.0)
    , mvacc(0.0)
    , mvtime(0.0)
    , coord(0)
    , relative(0)  {
  (void)_alloc;
    }



   typedef std::vector<float, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<float>> _pose_type;
  _pose_type pose;

   typedef float _mvvelo_type;
  _mvvelo_type mvvelo;

   typedef float _mvacc_type;
  _mvacc_type mvacc;

   typedef float _mvtime_type;
  _mvtime_type mvtime;

   typedef int16_t _coord_type;
  _coord_type coord;

   typedef int16_t _relative_type;
  _relative_type relative;





  typedef boost::shared_ptr< ::xarm_msgs::MoveAxisAngleRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::xarm_msgs::MoveAxisAngleRequest_<ContainerAllocator> const> ConstPtr;

}; // struct MoveAxisAngleRequest_

typedef ::xarm_msgs::MoveAxisAngleRequest_<std::allocator<void> > MoveAxisAngleRequest;

typedef boost::shared_ptr< ::xarm_msgs::MoveAxisAngleRequest > MoveAxisAngleRequestPtr;
typedef boost::shared_ptr< ::xarm_msgs::MoveAxisAngleRequest const> MoveAxisAngleRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::xarm_msgs::MoveAxisAngleRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::xarm_msgs::MoveAxisAngleRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::xarm_msgs::MoveAxisAngleRequest_<ContainerAllocator1> & lhs, const ::xarm_msgs::MoveAxisAngleRequest_<ContainerAllocator2> & rhs)
{
  return lhs.pose == rhs.pose &&
    lhs.mvvelo == rhs.mvvelo &&
    lhs.mvacc == rhs.mvacc &&
    lhs.mvtime == rhs.mvtime &&
    lhs.coord == rhs.coord &&
    lhs.relative == rhs.relative;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::xarm_msgs::MoveAxisAngleRequest_<ContainerAllocator1> & lhs, const ::xarm_msgs::MoveAxisAngleRequest_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace xarm_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::xarm_msgs::MoveAxisAngleRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::xarm_msgs::MoveAxisAngleRequest_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::xarm_msgs::MoveAxisAngleRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::xarm_msgs::MoveAxisAngleRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::xarm_msgs::MoveAxisAngleRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::xarm_msgs::MoveAxisAngleRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::xarm_msgs::MoveAxisAngleRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "5f222fa2eeda5e2b5482505e275dcd88";
  }

  static const char* value(const ::xarm_msgs::MoveAxisAngleRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x5f222fa2eeda5e2bULL;
  static const uint64_t static_value2 = 0x5482505e275dcd88ULL;
};

template<class ContainerAllocator>
struct DataType< ::xarm_msgs::MoveAxisAngleRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "xarm_msgs/MoveAxisAngleRequest";
  }

  static const char* value(const ::xarm_msgs::MoveAxisAngleRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::xarm_msgs::MoveAxisAngleRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# request: command specification for axis-angle motion executions.\n"
"# Units:\n"
"#	Linear: mm, mm/s, and mm/s^2.\n"
"#   Angular: radian.\n"
"#	time: sec\n"
"\n"
"# pose: target coordinate. \n"
"#	For Cartesian target: pose dimention is 6 for (x, y, z, rx, ry, rz)\n"
"\n"
"float32[] pose\n"
"\n"
"# mvvelo: (value range: 0 ~ 1000) specified maximum velocity during execution. linear (0 to 1000 mm/s)  or angular (range 0~1000 for 0 to 3.14 rad/s) velocity.\n"
"\n"
"float32 mvvelo\n"
"\n"
"# mvacc: specified maximum linear acceleration (mm/s^2) during execution. (angular acceleration is fixed currently).\n"
"\n"
"float32 mvacc\n"
"\n"
"# mvtime: currently do not have any special meaning, please just give it 0. \n"
"\n"
"float32 mvtime\n"
"\n"
"# coord: motion coordinate system indicator, base (0) or tool(1) coordinate.\n"
"\n"
"int16 coord\n"
"\n"
"# relative: indicator of given target is relative (1) or not (0, absolute)\n"
"\n"
"int16 relative\n"
"\n"
;
  }

  static const char* value(const ::xarm_msgs::MoveAxisAngleRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::xarm_msgs::MoveAxisAngleRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.pose);
      stream.next(m.mvvelo);
      stream.next(m.mvacc);
      stream.next(m.mvtime);
      stream.next(m.coord);
      stream.next(m.relative);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct MoveAxisAngleRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::xarm_msgs::MoveAxisAngleRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::xarm_msgs::MoveAxisAngleRequest_<ContainerAllocator>& v)
  {
    s << indent << "pose[]" << std::endl;
    for (size_t i = 0; i < v.pose.size(); ++i)
    {
      s << indent << "  pose[" << i << "]: ";
      Printer<float>::stream(s, indent + "  ", v.pose[i]);
    }
    s << indent << "mvvelo: ";
    Printer<float>::stream(s, indent + "  ", v.mvvelo);
    s << indent << "mvacc: ";
    Printer<float>::stream(s, indent + "  ", v.mvacc);
    s << indent << "mvtime: ";
    Printer<float>::stream(s, indent + "  ", v.mvtime);
    s << indent << "coord: ";
    Printer<int16_t>::stream(s, indent + "  ", v.coord);
    s << indent << "relative: ";
    Printer<int16_t>::stream(s, indent + "  ", v.relative);
  }
};

} // namespace message_operations
} // namespace ros

#endif // XARM_MSGS_MESSAGE_MOVEAXISANGLEREQUEST_H
