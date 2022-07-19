// Auto-generated. Do not edit!

// (in-package motor_ctl.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class vel {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.lv = null;
      this.rv = null;
    }
    else {
      if (initObj.hasOwnProperty('lv')) {
        this.lv = initObj.lv
      }
      else {
        this.lv = 0.0;
      }
      if (initObj.hasOwnProperty('rv')) {
        this.rv = initObj.rv
      }
      else {
        this.rv = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type vel
    // Serialize message field [lv]
    bufferOffset = _serializer.float32(obj.lv, buffer, bufferOffset);
    // Serialize message field [rv]
    bufferOffset = _serializer.float32(obj.rv, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type vel
    let len;
    let data = new vel(null);
    // Deserialize message field [lv]
    data.lv = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [rv]
    data.rv = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 8;
  }

  static datatype() {
    // Returns string type for a message object
    return 'motor_ctl/vel';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '2f2d9a30844403ccb0451dd87e709319';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32 lv
    float32 rv
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new vel(null);
    if (msg.lv !== undefined) {
      resolved.lv = msg.lv;
    }
    else {
      resolved.lv = 0.0
    }

    if (msg.rv !== undefined) {
      resolved.rv = msg.rv;
    }
    else {
      resolved.rv = 0.0
    }

    return resolved;
    }
};

module.exports = vel;
