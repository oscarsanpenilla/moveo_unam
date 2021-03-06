#!/usr/bin/env python
# license removed for brevity
import rospy
import csv
import numpy as np
from moveo_unam.msg import JointVariables

array = []


with open('/home/engelfuk/catkin_ws/src/moveo_unam/scripts/Trayectoria.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',',quotechar=" ")
    for row in reader:
        array.append(row)
array = np.array(array)
array = np.asfarray(array,float)  

def main():
    pub = rospy.Publisher('joint_variables', JointVariables, queue_size=10)
    rospy.init_node('inverse_kinematics', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    complete_trayectory = False
    while not rospy.is_shutdown():
        if(complete_trayectory == False):
            for value in array:
                joint_variables = JointVariables()
                joint_variables.theta1 = value[0]
                joint_variables.theta2 = value[1]
                joint_variables.theta3 = value[2]
                joint_variables.theta4 = value[3]
                joint_variables.theta5 = value[4]
                rospy.loginfo(joint_variables)
                pub.publish(joint_variables)
        #complete_trayectory = True
            
        
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
