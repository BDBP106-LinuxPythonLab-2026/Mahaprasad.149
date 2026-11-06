import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-20, 20, 1000)

f1 = np.log(1/np.cos(x)**2)
f2 = np.log(1/np.sin(x)**2)

plt.plot(x, f1, label="f1")
plt.plot(x, f2, label="f2")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Log Functions")
plt.legend()
plt.grid()
plt.ylim(-5, 10)
plt.show()
