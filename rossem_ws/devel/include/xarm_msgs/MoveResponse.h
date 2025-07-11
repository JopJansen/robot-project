// Generated by gencpp from file xarm_msgs/MoveResponse.msg
// DO NOT EDIT!


#ifndef XARM_MSGS_MESSAGE_MOVERESPONSE_H
#define XARM_MSGS_MESSAGE_MOVERESPONSE_H


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
struct MoveResponse_
{
  typedef MoveResponse_<ContainerAllocator> Type;

  MoveResponse_()
    : ret(0)
    , message()  {
    }
  MoveResponse_(const ContainerAllocator& _alloc)
    : ret(0)
    , message(_alloc)  {
  (void)_alloc;
    }



   typedef int16_t _ret_type;
  _ret_type ret;

   typedef std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> _message_type;
  _message_type message;





  typedef boost::shared_ptr< ::xarm_msgs::MoveResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::xarm_msgs::MoveResponse_<ContainerAllocator> const> ConstPtr;

}; // struct MoveResponse_

typedef ::xarm_msgs::MoveResponse_<std::allocator<void> > MoveResponse;

typedef boost::shared_ptr< ::xarm_msgs::MoveResponse > MoveResponsePtr;
typedef boost::shared_ptr< ::xarm_msgs::MoveResponse const> MoveResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::xarm_msgs::MoveResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::xarm_msgs::MoveResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::xarm_msgs::MoveResponse_<ContainerAllocator1> & lhs, const ::xarm_msgs::MoveResponse_<ContainerAllocator2> & rhs)
{
  return lhs.ret == rhs.ret &&
    lhs.message == rhs.message;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::xarm_msgs::MoveResponse_<ContainerAllocator1> & lhs, const ::xarm_msgs::MoveResponse_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace xarm_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::xarm_msgs::MoveResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::xarm_msgs::MoveResponse_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::xarm_msgs::MoveResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::xarm_msgs::MoveResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::xarm_msgs::MoveResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::xarm_msgs::MoveResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::xarm_msgs::MoveResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "76c68a2c5e109f4d6a4dc1cfc355f405";
  }

  static const char* value(const ::xarm_msgs::MoveResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x76c68a2c5e109f4dULL;
  static const uint64_t static_value2 = 0x6a4dc1cfc355f405ULL;
};

template<class ContainerAllocator>
struct DataType< ::xarm_msgs::MoveResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "xarm_msgs/MoveResponse";
  }

  static const char* value(const ::xarm_msgs::MoveResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::xarm_msgs::MoveResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "\n"
"# response: \n"
"#	ret is 0 for successful execution and others for errors or warnings occured\n"
"#	message is a string returned by function, indicating execution status.\n"
"\n"
"int16 ret\n"
"\n"
"string message\n"
;
  }

  static const char* value(const ::xarm_msgs::MoveResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::xarm_msgs::MoveResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.ret);
      stream.next(m.message);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct MoveResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::xarm_msgs::MoveResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::xarm_msgs::MoveResponse_<ContainerAllocator>& v)
  {
    s << indent << "ret: ";
    Printer<int16_t>::stream(s, indent + "  ", v.ret);
    s << indent << "message: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>::stream(s, indent + "  ", v.message);
  }
};

} // namespace message_operations
} // namespace ros

#endif // XARM_MSGS_MESSAGE_MOVERESPONSE_H
