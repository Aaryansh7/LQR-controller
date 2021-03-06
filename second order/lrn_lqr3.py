import numpy as np
from control import lqr
import matplotlib.pyplot as plt
from scipy import signal

A=[[0.0,1.0],
   [-0.25,-0.5]]
print(np.linalg.eig(A)[0]) #if negative real part then system is stable

B=[[0.0],[0.75]]
C=[[1.0,0.0]]
D=[0]
Q=[[1.0,0.0],
   [0.0,1.0]]
R=[1]

K,S,E=lqr(A,B,Q,R)
BK=np.dot(B,K)
AminusBK=np.subtract(A,BK)
sys2=signal.StateSpace(AminusBK,B,C,D)
t2,y2=signal.step(sys2)

plt.plot(t2,y2)
plt.show()