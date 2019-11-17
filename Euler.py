import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('Euler.dat')

plt.figure(figsize=(14,10))

plt.subplot(2,1,1)
plt.title("Euler")
plt.xlabel("t")
plt.ylabel("y0")
plt.plot(data[:,0],data[:,1])

plt.savefig("y0Vst.png")