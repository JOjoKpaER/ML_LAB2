import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return np.log((x*x+1)*np.exp(-1*abs(x)/10),
                  (1+np.tan((1/(1+np.power(np.sin(x), 2))))))


x = np.arange(-10.0, 10.0, 0.05)
y = f(x)
plt.plot(x, y)
plt.show()

