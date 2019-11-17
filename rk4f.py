import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('rk4f.dat')

plt.figure(figsize=(14,10))

plt.title("rk4 fric = 0.4")
plt.xlabel("t")
plt.ylabel("y0")
plt.plot(data[:,0],data[:,1])

plt.savefig("rk4fric.png")