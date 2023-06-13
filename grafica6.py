import matplotlib.pyplot as plt
import numpy as np
from numpy import sin


x = np.linspace(0, 2, 100)
def f(x):
    return(x*np.exp(-3*x))

def g(x):
    return(np.exp(-3*x)*(1-3*x))

lib, ax=plt.subplots()
line1 = ax.plot(x, f(x), linestyle = 'dashed', linewidth =3, color= 'c', markersize =10, label='linea 1')
line2 = ax.plot(x, g(x), linestyle = 'dotted', linewidth =3, color='m', markersize=10, label='linea 2' )
plt.legend(loc='upper left')
plt.title("h(t) = $xe^{-3x}   /   g(x) = e^{-3x}(1-3x)$")
plt.ylabel('Eje Y')
plt.xlabel('Eje X')
plt.grid(True)
plt.show()