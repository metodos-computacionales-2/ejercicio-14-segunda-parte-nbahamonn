import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('Rk4.dat')
data2 = np.loadtxt('Euler.dat')

plt.figure(figsize=(14,10))

plt.subplot(2,1,1)
plt.title("rk4")
plt.xlabel("t")
plt.ylabel("y0")
plt.plot(data[:,0],data[:,1])

plt.subplot(2,1,2)
plt.title("Comparacion Euler Vs rk4")
plt.xlabel("y0")
plt.ylabel("y1")
plt.plot(data[:,1],data[:,2], label = "rk4")
plt.plot(data2[:,1],data2[:,2], label = "Euler")
plt.legend()

plt.savefig("rk4.png")