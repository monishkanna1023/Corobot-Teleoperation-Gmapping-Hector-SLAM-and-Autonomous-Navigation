
(cl:in-package :asdf)

(defsystem "motor_ctl-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "vel" :depends-on ("_package_vel"))
    (:file "_package_vel" :depends-on ("_package"))
  ))