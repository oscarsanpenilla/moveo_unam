#!/usr/bin/env python
import rospy
from sympy import *
from kinematics_math import *
from moveo_unam.msg import JointVariables






def callback(data):
    x = px.subs({th1: data.theta1, th2: data.theta2, th3: data.theta3,
                th4: data.theta4,th5: data.theta5}).evalf()
    y = py.subs({th1: data.theta1, th2: data.theta2, th3: data.theta3,
                th4: data.theta4,th5: data.theta5}).evalf()
    z = pz.subs({th1: data.theta1, th2: data.theta2, th3: data.theta3,
                th4: data.theta4,th5: data.theta5}).evalf()
    print("---\nx: {}\ny: {}\nz: {}".format(x,y,z))
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('position', anonymous=True)

    rospy.Subscriber("joint_variables", JointVariables, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
