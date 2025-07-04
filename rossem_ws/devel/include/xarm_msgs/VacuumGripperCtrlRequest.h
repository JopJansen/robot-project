// Generated by gencpp from file xarm_msgs/VacuumGripperCtrlRequest.msg
// DO NOT EDIT!


#ifndef XARM_MSGS_MESSAGE_VACUUMGRIPPERCTRLREQUEST_H
#define XARM_MSGS_MESSAGE_VACUUMGRIPPERCTRLREQUEST_H


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
struct VacuumGripperCtrlRequest_
{
  typedef VacuumGripperCtrlRequest_<ContainerAllocator> Type;

  VacuumGripperCtrlRequest_()
    : on(false)
    , wait(false)
    , timeout(0.0)
    , delay_sec(0.0)
    , sync(false)
    , hardware_version(0)  {
    }
  VacuumGripperCtrlRequest_(const ContainerAllocator& _alloc)
    : on(false)
    , wait(false)
    , timeout(0.0)
    , delay_sec(0.0)
    , sync(false)
    , hardware_version(0)  {
  (void)_alloc;
    }



   typedef uint8_t _on_type;
  _on_type on;

   typedef uint8_t _wait_type;
  _wait_type wait;

   typedef float _timeout_type;
  _timeout_type timeout;

   typedef float _delay_sec_type;
  _delay_sec_type delay_sec;

   typedef uint8_t _sync_type;
  _sync_type sync;

   typedef int16_t _hardware_version_type;
  _hardware_version_type hardware_version;





  typedef boost::shared_ptr< ::xarm_msgs::VacuumGripperCtrlRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::xarm_msgs::VacuumGripperCtrlRequest_<ContainerAllocator> const> ConstPtr;

}; // struct VacuumGripperCtrlRequest_

typedef ::xarm_msgs::VacuumGripperCtrlRequest_<std::allocator<void> > VacuumGripperCtrlRequest;

typedef boost::shared_ptr< ::xarm_msgs::VacuumGripperCtrlRequest > VacuumGripperCtrlRequestPtr;
typedef boost::shared_ptr< ::xarm_msgs::VacuumGripperCtrlRequest const> VacuumGripperCtrlRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::xarm_msgs::VacuumGripperCtrlRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::xarm_msgs::VacuumGripperCtrlRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::xarm_msgs::VacuumGripperCtrlRequest_<ContainerAllocator1> & lhs, const ::xarm_msgs::VacuumGripperCtrlRequest_<ContainerAllocator2> & rhs)
{
  return lhs.on == rhs.on &&
    lhs.wait == rhs.wait &&
    lhs.timeout == rhs.timeout &&
    lhs.delay_sec == rhs.delay_sec &&
    lhs.sync == rhs.sync &&
    lhs.hardware_version == rhs.hardware_version;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::xarm_msgs::VacuumGripperCtrlRequest_<ContainerAllocator1> & lhs, const ::xarm_msgs::VacuumGripperCtrlRequest_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace xarm_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::xarm_msgs::VacuumGripperCtrlRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::xarm_msgs::VacuumGripperCtrlRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::xarm_msgs::VacuumGripperCtrlRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::xarm_msgs::VacuumGripperCtrlRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::xarm_msgs::VacuumGripperCtrlRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::xarm_msgs::VacuumGripperCtrlRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::xarm_msgs::VacuumGripperCtrlRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bc32f2abd5876101c06705ab6e53499a";
  }

  static const char* value(const ::xarm_msgs::VacuumGripperCtrlRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xbc32f2abd5876101ULL;
  static const uint64_t static_value2 = 0xc06705ab6e53499aULL;
};

template<class ContainerAllocator>
struct DataType< ::xarm_msgs::VacuumGripperCtrlRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "xarm_msgs/VacuumGripperCtrlRequest";
  }

  static const char* value(const ::xarm_msgs::VacuumGripperCtrlRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::xarm_msgs::VacuumGripperCtrlRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bool on\n"
"bool wait\n"
"float32 timeout\n"
"float32 delay_sec\n"
"# sync: whether to execute in the motion queue\n"
"bool sync\n"
"# hardware_version==1: Plug-in Connection, default\n"
"# hardware_version==2: Contact Connection\n"
"int16 hardware_version\n"
"\n"
;
  }

  static const char* value(const ::xarm_msgs::VacuumGripperCtrlRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::xarm_msgs::VacuumGripperCtrlRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.on);
      stream.next(m.wait);
      stream.next(m.timeout);
      stream.next(m.delay_sec);
      stream.next(m.sync);
      stream.next(m.hardware_version);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct VacuumGripperCtrlRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::xarm_msgs::VacuumGripperCtrlRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::xarm_msgs::VacuumGripperCtrlRequest_<ContainerAllocator>& v)
  {
    s << indent << "on: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.on);
    s << indent << "wait: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.wait);
    s << indent << "timeout: ";
    Printer<float>::stream(s, indent + "  ", v.timeout);
    s << indent << "delay_sec: ";
    Printer<float>::stream(s, indent + "  ", v.delay_sec);
    s << indent << "sync: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.sync);
    s << indent << "hardware_version: ";
    Printer<int16_t>::stream(s, indent + "  ", v.hardware_version);
  }
};

} // namespace message_operations
} // namespace ros

#endif // XARM_MSGS_MESSAGE_VACUUMGRIPPERCTRLREQUEST_H
