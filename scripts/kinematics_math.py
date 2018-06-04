#!/usr/bin/env python
from sympy import *

class Kinematics:
    
    def __init__(self):
    
        self.thx = symbols("theta_x")
        self.thy = symbols("theta_y")
        self.thz = symbols("theta_z")
        self.th1 = symbols("theta_1")
        self.th2 = symbols("theta_2")
        self.th3 = symbols("theta_3")
        self.th4 = symbols("theta_4")
        self.th5 = symbols("theta_5")

        self.x, self.y, self.z = symbols("x y z")
        self.th, self.d, self.a, self.alfa = symbols("theta d a alfa")
     
        self.l1 = 7
        self.l2 = 14
        self.l3 = 23
        self.l4 = 13
        self.l5 = 10 



    def Rx(self,th):
        return Matrix([
        [1,0,0,0],
        [0,cos(th),-sin(th),0],
        [0,sin(th),cos(th),0],
        [0,0,0,1]
        ])
    def Ry(self,th):
        return Matrix([
        [cos(th),0,sin(th),0],
        [0,1,0,0],
        [-sin(th),0,cos(th),0],
        [0,0,0,1]
        ])
    def Rz(self,th):
        return Matrix([
        [cos(th),-sin(th),0,0],
        [sin(th),cos(th),0,0],
        [0,0,1,0],
        [0,0,0,1]
        ])

    def Pxyz(self,x,y,z):
        return Matrix([
        [1,0,0,x],
        [0,1,0,y],
        [0,0,1,z],
        [0,0,0,1]
        ])
    def TDH(self,th,d,a,alfa):
        return self.Rz(th)*self.Pxyz(a,0,d)*self.Rx(alfa)
        
    def main(self):
        n = Matrix([0,0,0,1])
        A01 = self.TDH(self.th1,self.l1,0,-pi/2)
        A12 = self.TDH(self.th2-pi/2,0,self.l2,0)
        A23 = self.TDH(self.th3 + pi/2,0,0,pi/2)
        A34 = self.TDH(self.th4,self.l3 + self.l4,0,-pi/2)
        A45 = self.TDH(self.th5 -pi/2,0,self.l5,0)
        
        A02 = A01*A12
        A03 = A02*A23
        A04 = A03*A34
        A05 = A04*A45
        
        #joint1
        joint1 = {'j1x': A01[0,3] , 'j1y': A01[1,3] , 'j1z': A01[2,3]}
        #joint2
        joint2 = {'j2x': A02[0,3] , 'j2y': A02[1,3] , 'j2z': A02[2,3]}
        #joint3
        joint3 = {'j3x': A03[0,3] , 'j3y': A03[1,3] , 'j3z': A03[2,3]}
        #joint4
        joint4 = {'j4x': A04[0,3] , 'j4y': A04[1,3] , 'j4z': A04[2,3]}
        #joint5
        joint5 = {'j5x': A05[0,3] , 'j5y': A05[1,3] , 'j5z': A05[2,3]}

        return [joint1,joint2,joint3,joint4,joint5]
      


