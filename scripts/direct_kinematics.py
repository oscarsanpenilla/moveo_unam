#!/usr/bin/env python
# license removed for brevity
import rospy
import csv
import numpy as np
from moveo_unam.msg import JointVariables

array = []
with open('Trayectoria1.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',',quotechar=" ")
    for row in spamreader:
        array.append(row)
array = np.array(array)
array = np.asfarray(array,float)  

def main():
    pub = rospy.Publisher('joint_variables', JointVariables, queue_size=10)
    rospy.init_node('inverse_kinematics', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        joint_variables = JointVariables()
        for value in array:
            joint_variables.theta1 = value[0]
            joint_variables.theta2 = value[1]
            joint_variables.theta3 = value[2]
            joint_variables.theta4 = value[3]
            joint_variables.theta5 = value[4]
       
        rospy.loginfo(joint_variables)
        pub.publish(joint_variables)
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
