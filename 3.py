import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return x*x-x-6


x = np.arange(-10.0, 10.0, 0.05)
y = []
y0 = []
for i in x:
    y.append(f(i))
    y0.append(0)
plt.plot(x, y)
plt.plot(x, y0)
plt.show()

