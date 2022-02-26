import numpy as np
from numpy import sin,cos,matmul,trace,arccos
from numpy.linalg import matrix_power as power
from numpy import pi as pi
def vect(v):
    V = np.zeros([3, 1])
    V[0, 0] = v[2, 1]-v[1, 2]
    V[1, 0] = v[0, 2]-v[2, 0]
    V[2, 0] = v[1, 0]-v[0, 1]
    V = (1/2)*V
    return V
def CPM(n, v):
    V = np.zeros([3, 3],dtype=int)
    V[0, 1] = -v[2, n]
    V[0, 2] =  v[1, n]
    V[1, 0] =  v[2, n]
    V[1, 2] = -v[0, n]
    V[2, 0] = -v[1, n]
    V[2, 1] =  v[0, n]
    return V
e = list(map(int, input("Please insert your vector to rotate"+"\n").split(" ")))
p = np.array(e).reshape(3, 1)
e = list(map(int, input("Please insert your matrix of rotation axis vectors"+"\n").split(" ")))
e = np.array(e).reshape(3, 3)
phi = list(map(int, input("Please insert your rotation degree"+"\n").split(" ")))
Q_total = np.eye(3, dtype=int)
I = np.eye(3, dtype=int)
for i in range(3):
    E = CPM(i, e)
    Q = I + sin(phi[i]*pi/180)*E + (1-cos(phi[i]*pi/180))*(power(E, 2))
    Q_total = matmul(Q_total, Q)
##print(np.rint(matmul(Q_total, Q_total.transpose())))
##print(np.linalg.det(Q_total))
print("P_final="+"\n"+f"{np.around(matmul(Q_total, p),decimals=4)}")
phi_total = arccos((trace(Q_total)-1)/2)
print(f"Phi_total is: {phi_total*180/pi}")
if phi_total == 0:
    print("The rotation is invalid")
else:
    e_final = vect(Q_total)/sin(phi_total)
    print("e_total is:"+"\n"+f"{e_final}")