import time
import serial
from vpython import *
import numpy as np
from numpy import cos,sin

arduinoData = serial.Serial('com10', 115200)
time.sleep(1)

toRad = np.pi/180.0
toDeg = 1/toRad

scene.range=4
scene.background=color.white
# scene.forward=vector(-1,-1,-1)
bread_board=box(length=2,width=6,height=.2,color=color.white,opacity=0.25)
Arduino=box(pos=vector(0,-.125,1.5),length=1.5,width=2,height=.1,color=color.blue,opacity=0.25)
obj=compound([bread_board,Arduino])

x_axis=arrow(axis=vector(1,0,0),length=3,shaftwidth=0.1,color=color.red,opacity=1)
y_axis=arrow(axis=vector(0,1,0),length=3,shaftwidth=0.1,color=color.green,opacity=1)
z_axis=arrow(axis=vector(0,0,1),length=3,shaftwidth=0.1,color=color.blue,opacity=1)



def Quanterion(splitPacket):
    Q=[]
    Q.append(float(splitPacket[0]))
    Q.append(float(splitPacket[1]))
    Q.append(float(splitPacket[2]))
    Q.append(float(splitPacket[3]))
    q0 = Q[0]
    q1 = Q[1]
    q2 = Q[2]
    q3 = Q[3]
    r00 = 2 * (q0 * q0 + q1 * q1) - 1
    r01 = 2 * (q1 * q2 - q0 * q3)
    r02 = 2 * (q1 * q3 + q0 * q2)
    r10 = 2 * (q1 * q2 + q0 * q3)
    r11 = 2 * (q0 * q0 + q2 * q2) - 1
    r12 = 2 * (q2 * q3 - q0 * q1)
    r20 = 2 * (q1 * q3 - q0 * q2)
    r21 = 2 * (q2 * q3 + q0 * q1)
    r22 = 2 * (q0 * q0 + q3 * q3) - 1
     
    # 3x3 rotation matrix
    rotation_matrix = np.array([[r00, r01, r02],
                           [r10, r11, r12],
                           [r20, r21, r22]])
    final=np.matmul([[0,0,1],[1,0,0]],rotation_matrix)
    print(np.round(rotation_matrix))
    return final

def YRW(x):
    roll=float(x[0])*toRad
    pitch=float(x[1])*toRad
    yaw=float(x[2])*toRad
    Q_roll=np.array([[1,0,0],[0,cos(roll),-sin(roll)],[0,sin(roll),cos(roll)]])
    Q_pitch=np.array([[cos(pitch),0,sin(pitch)],[0,1,-0],[-sin(pitch),0,cos(pitch)]])
    roll_axis=np.matmul(Q_roll,[0,0,1])
    pitch_axis=np.matmul(Q_pitch,[0,0,1])
    total_axis=roll_axis+pitch_axis
    obj.up=vector(roll_axis[0],roll_axis[1],roll_axis[2])
    Q_yaw=np.array([[cos(yaw),-sin(yaw),0],[sin(yaw),cos(yaw),0],[0,0,1]])
    yaw_axis=np.matmul(Q_yaw,[1,0,0])
    print(yaw_axis)
    Q=np.array([[cos(roll)*cos(pitch)*cos(yaw)-sin(pitch)*sin(yaw)]])
    obj.axis=vector(yaw_axis[0],yaw_axis[1],yaw_axis[2])

    return

# Simulate your object using VPython

while True:
    
    while arduinoData.inWaiting() == 0:
        pass
    dataPacket = arduinoData.readline()
    try:
        dataPacket = str(dataPacket, 'utf-8')
        splitPacket = dataPacket.split(",")
        final = Quanterion(splitPacket)
        print(np.round(final))
        obj.up = vector(-final[0][0], -final[0][1], -final[0][2])
        obj.axis = vector(final[1][0], final[1][1], final[1][2])

        # Change the attributes of your object to syncronize it with real time motions

    except:
        print("selam")
    