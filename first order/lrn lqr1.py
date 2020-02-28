from control import lqr
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt


A=-4.0
B=2.0
C=1.0
D=0.0

Q=1.0
R=1.0

K,S,E=lqr(A,B,Q,R)
BK=np.dot(B,K)
AminusBK=np.subtract(A,BK)
sys1=signal.StateSpace(AminusBK,B,C,D)



t1,y1=signal.step(sys1)
plt.plot(t1,y1)
plt.show()




