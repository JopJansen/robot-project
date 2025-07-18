// Auto-generated. Do not edit!

// (in-package xarm_msgs.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class VeloMoveMsg {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.speeds = null;
      this.is_sync = null;
      this.is_tool_coord = null;
      this.duration = null;
    }
    else {
      if (initObj.hasOwnProperty('speeds')) {
        this.speeds = initObj.speeds
      }
      else {
        this.speeds = [];
      }
      if (initObj.hasOwnProperty('is_sync')) {
        this.is_sync = initObj.is_sync
      }
      else {
        this.is_sync = false;
      }
      if (initObj.hasOwnProperty('is_tool_coord')) {
        this.is_tool_coord = initObj.is_tool_coord
      }
      else {
        this.is_tool_coord = false;
      }
      if (initObj.hasOwnProperty('duration')) {
        this.duration = initObj.duration
      }
      else {
        this.duration = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type VeloMoveMsg
    // Serialize message field [speeds]
    bufferOffset = _arraySerializer.float32(obj.speeds, buffer, bufferOffset, null);
    // Serialize message field [is_sync]
    bufferOffset = _serializer.bool(obj.is_sync, buffer, bufferOffset);
    // Serialize message field [is_tool_coord]
    bufferOffset = _serializer.bool(obj.is_tool_coord, buffer, bufferOffset);
    // Serialize message field [duration]
    bufferOffset = _serializer.float32(obj.duration, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type VeloMoveMsg
    let len;
    let data = new VeloMoveMsg(null);
    // Deserialize message field [speeds]
    data.speeds = _arrayDeserializer.float32(buffer, bufferOffset, null)
    // Deserialize message field [is_sync]
    data.is_sync = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [is_tool_coord]
    data.is_tool_coord = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [duration]
    data.duration = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += 4 * object.speeds.length;
    return length + 10;
  }

  static datatype() {
    // Returns string type for a message object
    return 'xarm_msgs/VeloMoveMsg';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '3ff5ed26eb25726c663dac7efa05cc61';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # request: command specification for velocity executions.
    # Units:
    #	joint space/angles: radian/s
    #	Cartesian space: mm/s, radian/s.
    
    # speeds: the velocity list of the joints/tcp
    #   For velo_move_joint_timed topic: [joint1_velocity, ..., joint7_velocity]
    #   For velo_move_line_timed topic: [x_velocity, y_velocity, z_velocity, rx_velocity, ry_velocity, rz_velocity (axis-angle)]
    float32[] speeds
    
    # is_sync: this is special for velo_move_joint_timed topic, meaning whether all joints accelerate and decelerate synchronously, true for yes, false for no.
    # avaiable for topic velo_move_joint_timed
    bool is_sync
    
    # is_tool_coord: this is special for velo_move_line_timed topic, meaning whether motion is in tool coordinate(true) or not(false)
    # avaiable for topic velo_move_line_timed
    bool is_tool_coord
    
    # the maximum duration of the speed, over this time will automatically set the speed to 0
    #   duration > 0: seconds, indicates the maximum number of seconds that this speed can be maintained
    #   duration == 0: always effective, will not stop automativally
    #   duration < 0: only used to be compatible with the old protocol, equivalent to 0
    # avaiable for firmware_version >= 1.8.0
    float32 duration
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new VeloMoveMsg(null);
    if (msg.speeds !== undefined) {
      resolved.speeds = msg.speeds;
    }
    else {
      resolved.speeds = []
    }

    if (msg.is_sync !== undefined) {
      resolved.is_sync = msg.is_sync;
    }
    else {
      resolved.is_sync = false
    }

    if (msg.is_tool_coord !== undefined) {
      resolved.is_tool_coord = msg.is_tool_coord;
    }
    else {
      resolved.is_tool_coord = false
    }

    if (msg.duration !== undefined) {
      resolved.duration = msg.duration;
    }
    else {
      resolved.duration = 0.0
    }

    return resolved;
    }
};

module.exports = VeloMoveMsg;
