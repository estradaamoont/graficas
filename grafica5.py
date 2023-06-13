import matplotlib.pyplot as plt
import numpy as np
from numpy import sin
from numpy import cos
import math


x = np.linspace(0, 4*math.pi, 200)
def s(x):
    return(np.cos(2*x)+np.sin(3*x))

def v(x):
    return(-2*np.sin(2*x)+3*np.cos(3*x))

lib, ax=plt.subplots()
line1 = ax.plot(x, s(x), linestyle = '--', linewidth =3, color= 'b', markersize =10, label='Azul')
line2 = ax.plot(x, v(x), linestyle = ':', linewidth =3, color='r', markersize=10, label='Rojo' )
plt.legend(loc='lower center')
plt.title("$s(x)= cos(2x)+sen(3x), v(x)= -2sen(2x)+3cos(3x)$")
plt.ylabel('Eje Y')
plt.xlabel('Eje X')
plt.grid(True)
plt.show()