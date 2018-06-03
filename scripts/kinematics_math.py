#!/usr/bin/env python
from sympy import *

thx = symbols("theta_x")
thy = symbols("theta_y")
thz = symbols("theta_z")
th1 = symbols("theta_1")
th2 = symbols("theta_2")
th3 = symbols("theta_3")
th4 = symbols("theta_4")
th5 = symbols("theta_5")

x, y, z = symbols("x y z")
th, d, a, alfa = symbols("theta d a alfa")
l1 = 166.5
l2 = 221
l3 = 127
l4 = 96
l5 = 128 



def Rx(th):
    return Matrix([
    [1,0,0,0],
    [0,cos(th),-sin(th),0],
    [0,sin(th),cos(th),0],
    [0,0,0,1]
    ])
def Ry(th):
    return Matrix([
    [cos(th),0,sin(th),0],
    [0,1,0,0],
    [-sin(th),0,cos(th),0],
    [0,0,0,1]
    ])
def Rz(th):
    return Matrix([
    [cos(th),-sin(th),0,0],
    [sin(th),cos(th),0,0],
    [0,0,1,0],
    [0,0,0,1]
    ])

def Pxyz(x,y,z):
    return Matrix([
    [1,0,0,x],
    [0,1,0,y],
    [0,0,1,z],
    [0,0,0,1]
    ])
def TDH(th,d,a,alfa):
    return Rz(th)*Pxyz(a,0,d)*Rx(alfa)
    
n = Matrix([0,0,0,1])

A01 = TDH(th1,l1,0,-pi/2)
A12 = TDH(th2-pi/2,0,l2,0)
A23 = TDH(th3 + pi/2,0,0,pi/2)
A34 = TDH(th4,l3 + l4,0,-pi/2)
A45 = TDH(th5 -pi/2,0,l5,0)

A02 = A01*A12
A03 = A02*A23
A04 = A03*A34
A05 = A04*A45

px = A05[0,3]
py = A05[1,3]
pz = A05[2,3]


