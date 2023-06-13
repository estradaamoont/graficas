import matplotlib.pyplot as plt
import numpy as np
from numpy import sin
from numpy import cos
import math


t = np.linspace(0, 4*math.pi, 100)
def f(t):
    return(np.sin(3*t)*np.cos(2*t))

def g(t):
    return(1/2*np.cos(t)+5/2*np.cos(5*t))

lib, ax=plt.subplots()
line1 = ax.plot(t, f(t), linestyle = 'dashdot', linewidth =3, color= 'c', markersize =10, label='cian')
line2 = ax.plot(t, g(t), linestyle = '--', linewidth =3, color='m', markersize=10, label='magenta' )
plt.legend(loc='lower right')
plt.title("$ f(t)=sin(3t)cos(2t), g(t)=1/2cos(t)+5/2cos(5t)$")
plt.ylabel('Eje Y')
plt.xlabel('Eje X')
plt.grid(True)
plt.show()