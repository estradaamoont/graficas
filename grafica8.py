import matplotlib.pyplot as plt
import numpy as np
from numpy import sin
from numpy import cos
import math


t = np.linspace(0, 2*math.pi, 100)
def x(t):
    return((1+2*np.sin(t))*np.cos(t))

def y(t):
    return(1+2*np.sin(t)*np.sin(t))

lib, ax=plt.subplots()
line1 = ax.plot(t, x(t), linestyle = 'dotted', linewidth =1, color= 'c', markersize =8, label='cian')
line2 = ax.plot(t, y(t), linestyle = 'solid', linewidth =1, color='m', markersize=8, label='magenta' )
plt.legend(loc='center')
plt.title("$ x(t)=(1+2sen(t))co(t), y(t)=(1+2sen(t))sin(t)$")
plt.ylabel('Eje Y')
plt.xlabel('Eje X')
plt.grid(True)
plt.show()