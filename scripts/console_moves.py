#!/usr/bin/env python
# license removed for brevity
import rospy
from moveo_unam.msg import JointVariables

def main():
    pub = rospy.Publisher('joint_variables', JointVariables, queue_size=10)
    rospy.init_node('inverse_kinematics', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        joint_variables = JointVariables()
        joint_variables.theta1 = 500
        joint_variables.theta2 = 0
        joint_variables.theta3 = 0
        joint_variables.theta4 = 0
        joint_variables.theta5 = 0
       
        rospy.loginfo(joint_variables)
        pub.publish(joint_variables)
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
