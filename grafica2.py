import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 5, 100)
gx = 2*x*x - 8*x - 11
plt.plot(x, gx, 'o', linewidth=10, color='r')
plt.title('$G(x) = 2x^2-8x-11$')
plt.xlabel('Eje X', fontsize=10)
plt.ylabel('Eje Y', fontsize=10)
a = plt.gca()
plt.grid(True)
plt.show()
