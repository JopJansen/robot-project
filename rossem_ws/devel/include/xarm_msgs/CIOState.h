// Generated by gencpp from file xarm_msgs/CIOState.msg
// DO NOT EDIT!


#ifndef XARM_MSGS_MESSAGE_CIOSTATE_H
#define XARM_MSGS_MESSAGE_CIOSTATE_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>

namespace xarm_msgs
{
template <class ContainerAllocator>
struct CIOState_
{
  typedef CIOState_<ContainerAllocator> Type;

  CIOState_()
    : header()
    , state(0)
    , code(0)
    , input_digitals()
    , output_digitals()
    , input_analogs()
    , output_analogs()
    , input_conf()
    , output_conf()  {
      input_digitals.assign(0);

      output_digitals.assign(0);

      input_analogs.assign(0.0);

      output_analogs.assign(0.0);

      input_conf.assign(0);

      output_conf.assign(0);
  }
  CIOState_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , state(0)
    , code(0)
    , input_digitals()
    , output_digitals()
    , input_analogs()
    , output_analogs()
    , input_conf()
    , output_conf()  {
  (void)_alloc;
      input_digitals.assign(0);

      output_digitals.assign(0);

      input_analogs.assign(0.0);

      output_analogs.assign(0.0);

      input_conf.assign(0);

      output_conf.assign(0);
  }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef int16_t _state_type;
  _state_type state;

   typedef int16_t _code_type;
  _code_type code;

   typedef boost::array<uint16_t, 2>  _input_digitals_type;
  _input_digitals_type input_digitals;

   typedef boost::array<uint16_t, 2>  _output_digitals_type;
  _output_digitals_type output_digitals;

   typedef boost::array<float, 2>  _input_analogs_type;
  _input_analogs_type input_analogs;

   typedef boost::array<float, 2>  _output_analogs_type;
  _output_analogs_type output_analogs;

   typedef boost::array<uint8_t, 16>  _input_conf_type;
  _input_conf_type input_conf;

   typedef boost::array<uint8_t, 16>  _output_conf_type;
  _output_conf_type output_conf;





  typedef boost::shared_ptr< ::xarm_msgs::CIOState_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::xarm_msgs::CIOState_<ContainerAllocator> const> ConstPtr;

}; // struct CIOState_

typedef ::xarm_msgs::CIOState_<std::allocator<void> > CIOState;

typedef boost::shared_ptr< ::xarm_msgs::CIOState > CIOStatePtr;
typedef boost::shared_ptr< ::xarm_msgs::CIOState const> CIOStateConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::xarm_msgs::CIOState_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::xarm_msgs::CIOState_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::xarm_msgs::CIOState_<ContainerAllocator1> & lhs, const ::xarm_msgs::CIOState_<ContainerAllocator2> & rhs)
{
  return lhs.header == rhs.header &&
    lhs.state == rhs.state &&
    lhs.code == rhs.code &&
    lhs.input_digitals == rhs.input_digitals &&
    lhs.output_digitals == rhs.output_digitals &&
    lhs.input_analogs == rhs.input_analogs &&
    lhs.output_analogs == rhs.output_analogs &&
    lhs.input_conf == rhs.input_conf &&
    lhs.output_conf == rhs.output_conf;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::xarm_msgs::CIOState_<ContainerAllocator1> & lhs, const ::xarm_msgs::CIOState_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace xarm_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::xarm_msgs::CIOState_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::xarm_msgs::CIOState_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::xarm_msgs::CIOState_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::xarm_msgs::CIOState_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::xarm_msgs::CIOState_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::xarm_msgs::CIOState_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::xarm_msgs::CIOState_<ContainerAllocator> >
{
  static const char* value()
  {
    return "2a51ddec3163bc4c38eaa278474b2dc1";
  }

  static const char* value(const ::xarm_msgs::CIOState_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x2a51ddec3163bc4cULL;
  static const uint64_t static_value2 = 0x38eaa278474b2dc1ULL;
};

template<class ContainerAllocator>
struct DataType< ::xarm_msgs::CIOState_<ContainerAllocator> >
{
  static const char* value()
  {
    return "xarm_msgs/CIOState";
  }

  static const char* value(const ::xarm_msgs::CIOState_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::xarm_msgs::CIOState_<ContainerAllocator> >
{
  static const char* value()
  {
    return "Header header\n"
"\n"
"# contorller gpio module state\n"
"int16 state\n"
"\n"
"# controller gpio module error code\n"
"int16 code\n"
"\n"
"# input_digitals[0]: digital input functional gpio state\n"
"# input_digitals[1]: digital input configuring gpio state\n"
"#    CI0: (input_digitals[1] >> 0) & 0x0001\n"
"#    CI1: (input_digitals[1] >> 1) & 0x0001\n"
"#    CI7: (input_digitals[1] >> 7) & 0x0001\n"
"#    DI0: (input_digitals[1] >> 8) & 0x0001\n"
"#    DI1: (input_digitals[1] >> 9) & 0x0001\n"
"#    DI7: (input_digitals[1] >> 15) & 0x0001\n"
"uint16[2] input_digitals\n"
"\n"
"# output_digitals[0]: digital output functional gpio state\n"
"# output_digitals[1]: digital output configuring gpio state\n"
"#    CO0: (output_digitals[1] >> 0) & 0x0001\n"
"#    CO1: (output_digitals[1] >> 1) & 0x0001\n"
"#    CO7: (output_digitals[1] >> 7) & 0x0001\n"
"#    DO0: (output_digitals[1] >> 8) & 0x0001\n"
"#    DO1: (output_digitals[1] >> 9) & 0x0001\n"
"#    DO7: (output_digitals[1] >> 15) & 0x0001\n"
"uint16[2] output_digitals\n"
"\n"
"# input_analogs[0]: the value of AI0\n"
"# input_analogs[1]: the value of AI1\n"
"float32[2] input_analogs\n"
"\n"
"# output_analogs[0]: the value of AO0\n"
"# output_analogs[1]: the value of AO1\n"
"float32[2] output_analogs\n"
"\n"
"# digital input functional info\n"
"uint8[16] input_conf\n"
"\n"
"# digital output functional info\n"
"uint8[16] output_conf\n"
"================================================================================\n"
"MSG: std_msgs/Header\n"
"# Standard metadata for higher-level stamped data types.\n"
"# This is generally used to communicate timestamped data \n"
"# in a particular coordinate frame.\n"
"# \n"
"# sequence ID: consecutively increasing ID \n"
"uint32 seq\n"
"#Two-integer timestamp that is expressed as:\n"
"# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n"
"# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n"
"# time-handling sugar is provided by the client library\n"
"time stamp\n"
"#Frame this data is associated with\n"
"string frame_id\n"
;
  }

  static const char* value(const ::xarm_msgs::CIOState_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::xarm_msgs::CIOState_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.state);
      stream.next(m.code);
      stream.next(m.input_digitals);
      stream.next(m.output_digitals);
      stream.next(m.input_analogs);
      stream.next(m.output_analogs);
      stream.next(m.input_conf);
      stream.next(m.output_conf);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct CIOState_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::xarm_msgs::CIOState_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::xarm_msgs::CIOState_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "state: ";
    Printer<int16_t>::stream(s, indent + "  ", v.state);
    s << indent << "code: ";
    Printer<int16_t>::stream(s, indent + "  ", v.code);
    s << indent << "input_digitals[]" << std::endl;
    for (size_t i = 0; i < v.input_digitals.size(); ++i)
    {
      s << indent << "  input_digitals[" << i << "]: ";
      Printer<uint16_t>::stream(s, indent + "  ", v.input_digitals[i]);
    }
    s << indent << "output_digitals[]" << std::endl;
    for (size_t i = 0; i < v.output_digitals.size(); ++i)
    {
      s << indent << "  output_digitals[" << i << "]: ";
      Printer<uint16_t>::stream(s, indent + "  ", v.output_digitals[i]);
    }
    s << indent << "input_analogs[]" << std::endl;
    for (size_t i = 0; i < v.input_analogs.size(); ++i)
    {
      s << indent << "  input_analogs[" << i << "]: ";
      Printer<float>::stream(s, indent + "  ", v.input_analogs[i]);
    }
    s << indent << "output_analogs[]" << std::endl;
    for (size_t i = 0; i < v.output_analogs.size(); ++i)
    {
      s << indent << "  output_analogs[" << i << "]: ";
      Printer<float>::stream(s, indent + "  ", v.output_analogs[i]);
    }
    s << indent << "input_conf[]" << std::endl;
    for (size_t i = 0; i < v.input_conf.size(); ++i)
    {
      s << indent << "  input_conf[" << i << "]: ";
      Printer<uint8_t>::stream(s, indent + "  ", v.input_conf[i]);
    }
    s << indent << "output_conf[]" << std::endl;
    for (size_t i = 0; i < v.output_conf.size(); ++i)
    {
      s << indent << "  output_conf[" << i << "]: ";
      Printer<uint8_t>::stream(s, indent + "  ", v.output_conf[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // XARM_MSGS_MESSAGE_CIOSTATE_H
