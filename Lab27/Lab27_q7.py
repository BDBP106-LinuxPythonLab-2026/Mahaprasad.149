import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 1000)

for s in [1, 1.5, 2]:
    g = (1/(s*np.sqrt(2*np.pi))) * np.exp(-x**2/(2*s**2))
    plt.plot(x, g, label=f"sigma={s}")

plt.xlabel("x")
plt.ylabel("g(x)")
plt.title("Gaussian Distribution")
plt.legend()
plt.grid()
plt.show()
