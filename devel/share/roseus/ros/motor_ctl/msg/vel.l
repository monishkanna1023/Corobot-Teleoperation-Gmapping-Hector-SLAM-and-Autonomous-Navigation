;; Auto-generated. Do not edit!


(when (boundp 'motor_ctl::vel)
  (if (not (find-package "MOTOR_CTL"))
    (make-package "MOTOR_CTL"))
  (shadow 'vel (find-package "MOTOR_CTL")))
(unless (find-package "MOTOR_CTL::VEL")
  (make-package "MOTOR_CTL::VEL"))

(in-package "ROS")
;;//! \htmlinclude vel.msg.html


(defclass motor_ctl::vel
  :super ros::object
  :slots (_lv _rv ))

(defmethod motor_ctl::vel
  (:init
   (&key
    ((:lv __lv) 0.0)
    ((:rv __rv) 0.0)
    )
   (send-super :init)
   (setq _lv (float __lv))
   (setq _rv (float __rv))
   self)
  (:lv
   (&optional __lv)
   (if __lv (setq _lv __lv)) _lv)
  (:rv
   (&optional __rv)
   (if __rv (setq _rv __rv)) _rv)
  (:serialization-length
   ()
   (+
    ;; float32 _lv
    4
    ;; float32 _rv
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _lv
       (sys::poke _lv (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _rv
       (sys::poke _rv (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _lv
     (setq _lv (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _rv
     (setq _rv (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get motor_ctl::vel :md5sum-) "2f2d9a30844403ccb0451dd87e709319")
(setf (get motor_ctl::vel :datatype-) "motor_ctl/vel")
(setf (get motor_ctl::vel :definition-)
      "float32 lv
float32 rv

")



(provide :motor_ctl/vel "2f2d9a30844403ccb0451dd87e709319")


