import numpy as np
from control import lqr
from scipy import signal
import matplotlib.pyplot as plt

A=[[-3.0,0.0],
   [-2.0,-3.0]]
B=[[4.0],[0.0]]
C=[[0.5,0.5]]
D=[0.0]
Q=[[8.0,0.0],
   [0.0,1.0]]
R=[1.0]

K,S,E=lqr(A,B,Q,R)
BK=np.dot(B,K)
AminusBK=np.subtract(A,BK)
sys2=signal.StateSpace(AminusBK,B,C,D)
t2,y2=signal.step(sys2)

plt.plot(t2,y2)
plt.show()
