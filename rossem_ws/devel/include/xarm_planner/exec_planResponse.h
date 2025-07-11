// Generated by gencpp from file xarm_planner/exec_planResponse.msg
// DO NOT EDIT!


#ifndef XARM_PLANNER_MESSAGE_EXEC_PLANRESPONSE_H
#define XARM_PLANNER_MESSAGE_EXEC_PLANRESPONSE_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace xarm_planner
{
template <class ContainerAllocator>
struct exec_planResponse_
{
  typedef exec_planResponse_<ContainerAllocator> Type;

  exec_planResponse_()
    : success(false)  {
    }
  exec_planResponse_(const ContainerAllocator& _alloc)
    : success(false)  {
  (void)_alloc;
    }



   typedef uint8_t _success_type;
  _success_type success;





  typedef boost::shared_ptr< ::xarm_planner::exec_planResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::xarm_planner::exec_planResponse_<ContainerAllocator> const> ConstPtr;

}; // struct exec_planResponse_

typedef ::xarm_planner::exec_planResponse_<std::allocator<void> > exec_planResponse;

typedef boost::shared_ptr< ::xarm_planner::exec_planResponse > exec_planResponsePtr;
typedef boost::shared_ptr< ::xarm_planner::exec_planResponse const> exec_planResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::xarm_planner::exec_planResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::xarm_planner::exec_planResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::xarm_planner::exec_planResponse_<ContainerAllocator1> & lhs, const ::xarm_planner::exec_planResponse_<ContainerAllocator2> & rhs)
{
  return lhs.success == rhs.success;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::xarm_planner::exec_planResponse_<ContainerAllocator1> & lhs, const ::xarm_planner::exec_planResponse_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace xarm_planner

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::xarm_planner::exec_planResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::xarm_planner::exec_planResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::xarm_planner::exec_planResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::xarm_planner::exec_planResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::xarm_planner::exec_planResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::xarm_planner::exec_planResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::xarm_planner::exec_planResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "358e233cde0c8a8bcfea4ce193f8fc15";
  }

  static const char* value(const ::xarm_planner::exec_planResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x358e233cde0c8a8bULL;
  static const uint64_t static_value2 = 0xcfea4ce193f8fc15ULL;
};

template<class ContainerAllocator>
struct DataType< ::xarm_planner::exec_planResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "xarm_planner/exec_planResponse";
  }

  static const char* value(const ::xarm_planner::exec_planResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::xarm_planner::exec_planResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bool success\n"
;
  }

  static const char* value(const ::xarm_planner::exec_planResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::xarm_planner::exec_planResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.success);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct exec_planResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::xarm_planner::exec_planResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::xarm_planner::exec_planResponse_<ContainerAllocator>& v)
  {
    s << indent << "success: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.success);
  }
};

} // namespace message_operations
} // namespace ros

#endif // XARM_PLANNER_MESSAGE_EXEC_PLANRESPONSE_H
