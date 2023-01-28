# Corobot ROS Kinetic stack

**The system ran on Ubuntu Xenial Xerus 16.04 LTS version. ROS Kinetic which supported Ubuntu 16.04, was also installed. All the necessary drivers for the Phidget boards, for the LiDAR and an IDE to make our working process seamless were installed.**

## Abstract
This is the final year Engineering project of K Elamparithi, Monish Kanna R and Deepika J. SASTRA University '22.
Guided by prof. Dr. Manigandan, Dept. of EIE.
The group revived an old Coroware CoroBot and implemented teleoperation with a differential drive. 
Hector SLAM and Gmapping were implemented subsequently. Finally a simple obstacle avoidance algorithm was implemented.

## System Overview
<p align="center">
  <img src="https://user-images.githubusercontent.com/59819164/215282088-63bd709a-e9d1-44f2-994d-ea69c5da6e7f.png" />
</p>


We started with a base CoroWare Corobot. It had an integrated system that ran on an Intel Atom N2800 and had 4GB of DDR3 memory. The boot drive was a WD 320GB hard drive. It also had an Intel Wi-Fi card. It had 2 DC Motors (12V), 2 Hall effect encoders connected to the motors and a Hokuyo URG-04LX-UG01 LiDAR up top. The LiDAR was easy to interface with a mini–USB B cable.

<p align="center">
  <img src="https://user-images.githubusercontent.com/59819164/215282118-a8c9812e-fd1b-48be-9cf6-953c8afb955f.png" />
  <img src="https://user-images.githubusercontent.com/59819164/215282125-6d981d35-1976-4197-aaba-47e85e49d309.png" />
</p>

For the integration of the motors and encoders with the system, respective Phidget boards were used. 
PhidgetMotorControl HC 1064, a high current motor control Phidget which could drive 2 DC motors, was used to interface the motors. PhidgetEncoder HighSpeed 1047, a 4-input encoder board, was used to interface the encoders.
Since there was a limitation with the number of USB ports on the system, PhidgetInterfaceKit 1018, a Phidgets workhorse with 8 digital inputs, 8 digital outputs 6 USBs and 8 analogue voltage inputs, was used as a bridge between motor control and encoder board and the system.

