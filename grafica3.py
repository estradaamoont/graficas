import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(-1, 5, 300)
def f(t):
    return (t*np.exp(-2*t))

plt.plot(t, f(t), '-', linewidth =3, color= 'k', markersize =10)
plt.title("f(t) = $te^{-2t}$")
plt.ylabel('Eje Y')
plt.xlabel('Eje X')
plt.grid(True)
plt.show()