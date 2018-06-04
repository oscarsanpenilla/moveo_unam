#!/usr/bin/env python
import rospy
from sympy import *
from kinematics_math import *
from moveo_unam.msg import JointVariables
from geometry_msgs.msg import PointStamped
from std_msgs.msg import Header


class Position(Kinematics):
    
    def __init__(self):
        
        
        self.k = Kinematics()
        self.joints = self.k.main()
        
        self.j1x = self.joints[0]['j1x']
        self.j1y = self.joints[0]['j1y']
        self.j1z = self.joints[0]['j1z']
        self.j2x = self.joints[1]['j2x']
        self.j2y = self.joints[1]['j2y']
        self.j2z = self.joints[1]['j2z']
        self.j3x = self.joints[2]['j3x']
        self.j3y = self.joints[2]['j3y']
        self.j3z = self.joints[2]['j3z']
        self.j4x = self.joints[3]['j4x']
        self.j4y = self.joints[3]['j4y']
        self.j4z = self.joints[3]['j4z']
        self.j5x = self.joints[4]['j5x']
        self.j5y = self.joints[4]['j5y']
        self.j5z = self.joints[4]['j5z']
        
        self.j1x_ = 0.0
        self.j1y_ = 0.0
        self.j1z_ = 0.0
        self.j2x_ = 0.0
        self.j2y_ = 0.0
        self.j2z_ = 0.0
        self.j3x_ = 0.0
        self.j3y_ = 0.0
        self.j3z_ = 0.0
        self.j4x_ = 0.0
        self.j4y_ = 0.0
        self.j4z_ = 0.0
        self.j5x_ = 0.0
        self.j5y_ = 0.0
        self.j5z_ = 0.0      
            
        rospy.init_node('position', anonymous=True)
        self.pub = rospy.Publisher('position_variables', PointStamped, queue_size=10)
        rospy.Subscriber("joint_variables", JointVariables, self.callback)
        
  
    def callback(self,msg):
        sol = {'theta_1':msg.theta1,'theta_2':msg.theta2,'theta_3':msg.theta3,'theta_4':msg.theta4,'theta_5':msg.theta5}

        self.j1x_ = self.j1x.subs(sol).evalf()
        self.j1y_ = self.j1y.subs(sol).evalf()
        self.j1z_ = self.j1z.subs(sol).evalf()
        self.j2x_ = self.j2x.subs(sol).evalf()
        self.j2y_ = self.j2y.subs(sol).evalf()
        self.j2z_ = self.j2z.subs(sol).evalf()
        self.j3x_ = self.j3x.subs(sol).evalf()
        self.j3y_ = self.j3y.subs(sol).evalf()
        self.j3z_ = self.j3z.subs(sol).evalf()
        self.j4x_ = self.j4x.subs(sol).evalf()
        self.j4y_ = self.j4y.subs(sol).evalf()
        self.j4z_ = self.j4z.subs(sol).evalf()
        self.j5x_ = self.j5x.subs(sol).evalf()
        self.j5y_ = self.j5y.subs(sol).evalf()
        self.j5z_ = self.j5z.subs(sol).evalf()
        
        
    def run(self):
        
        
        r = rospy.Rate(10)
        while not rospy.is_shutdown():
            #joint 1
            joint1 = PointStamped()
            joint1.header.frame_id = "joint 1"
            joint1.header.stamp = rospy.Time.now()
            joint1.point.x = self.j1x_
            joint1.point.y = self.j1y_
            joint1.point.z = self.j1z_
            #joint 1
            joint2 = PointStamped()
            joint2.header.frame_id = "joint 2"
            joint2.header.stamp = rospy.Time.now()
            joint2.point.x = self.j2x_
            joint2.point.y = self.j2y_
            joint2.point.z = self.j2z_
            #joint 1
            joint3 = PointStamped()
            joint3.header.frame_id = "joint 3"
            joint3.header.stamp = rospy.Time.now()
            joint3.point.x = self.j3x_
            joint3.point.y = self.j3y_
            joint3.point.z = self.j3z_
            #joint 1
            joint4 = PointStamped()
            joint4.header.frame_id = "joint 4"
            joint4.header.stamp = rospy.Time.now()
            joint4.point.x = self.j4x_
            joint4.point.y = self.j4y_
            joint4.point.z = self.j4z_
            #joint 1
            joint5 = PointStamped()
            joint5.header.frame_id = "joint 5"
            joint5.header.stamp = rospy.Time.now()
            joint5.point.x = self.j5x_
            joint5.point.y = self.j5y_
            joint5.point.z = self.j5z_
            
            self.pub.publish(joint1)
            self.pub.publish(joint2)
            self.pub.publish(joint3)
            self.pub.publish(joint4)
            self.pub.publish(joint5)
            r.sleep()


if __name__ == '__main__':
    pos = Position()
    pos.run()
    #listener()
    
    
    
    
    
