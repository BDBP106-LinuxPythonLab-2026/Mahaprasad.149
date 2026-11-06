import numpy as np
import matplotlib.pyplot as plt
temps = np.arange(20, 71,5)
activity=np.array([12, 20, 35,52, 70, 85, 92, 78, 45, 18, 5 ])
opt=temps[np.argmax(activity)]

plt.plot(temps, activity,'o-')
plt.axvline(opt, linestyle='--')
plt.annotate('peak at 50(oC)', (opt,92))
plt.xlabel('Temperature')
plt.ylabel('Activity')
plt.title('activity vs temp')
plt.show()


print(opt)