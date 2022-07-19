; Auto-generated. Do not edit!


(cl:in-package motor_ctl-msg)


;//! \htmlinclude vel.msg.html

(cl:defclass <vel> (roslisp-msg-protocol:ros-message)
  ((lv
    :reader lv
    :initarg :lv
    :type cl:float
    :initform 0.0)
   (rv
    :reader rv
    :initarg :rv
    :type cl:float
    :initform 0.0))
)

(cl:defclass vel (<vel>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <vel>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'vel)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name motor_ctl-msg:<vel> is deprecated: use motor_ctl-msg:vel instead.")))

(cl:ensure-generic-function 'lv-val :lambda-list '(m))
(cl:defmethod lv-val ((m <vel>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader motor_ctl-msg:lv-val is deprecated.  Use motor_ctl-msg:lv instead.")
  (lv m))

(cl:ensure-generic-function 'rv-val :lambda-list '(m))
(cl:defmethod rv-val ((m <vel>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader motor_ctl-msg:rv-val is deprecated.  Use motor_ctl-msg:rv instead.")
  (rv m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <vel>) ostream)
  "Serializes a message object of type '<vel>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'lv))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'rv))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <vel>) istream)
  "Deserializes a message object of type '<vel>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'lv) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'rv) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<vel>)))
  "Returns string type for a message object of type '<vel>"
  "motor_ctl/vel")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'vel)))
  "Returns string type for a message object of type 'vel"
  "motor_ctl/vel")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<vel>)))
  "Returns md5sum for a message object of type '<vel>"
  "2f2d9a30844403ccb0451dd87e709319")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'vel)))
  "Returns md5sum for a message object of type 'vel"
  "2f2d9a30844403ccb0451dd87e709319")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<vel>)))
  "Returns full string definition for message of type '<vel>"
  (cl:format cl:nil "float32 lv~%float32 rv~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'vel)))
  "Returns full string definition for message of type 'vel"
  (cl:format cl:nil "float32 lv~%float32 rv~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <vel>))
  (cl:+ 0
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <vel>))
  "Converts a ROS message object to a list"
  (cl:list 'vel
    (cl:cons ':lv (lv msg))
    (cl:cons ':rv (rv msg))
))
