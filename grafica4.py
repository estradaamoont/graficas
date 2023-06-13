import matplotlib.pyplot as plt
import numpy as np
from numpy import sin

t = np.linspace(0, 24, 250)
def h(t):
    return(np.exp(-0.1*t)*sin(2*t))

plt.plot(t, h(t), '-', linewidth =3, color= 'g', markersize =10)
plt.title("h(t) = $e^{-0.1t}sen(2t)$")
plt.ylabel('Eje Y')
plt.xlabel('Eje X')
plt.grid(True)
plt.show()