import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('rk4f.dat') 

plt.figure(figsize=(14,10))

plt.subplot(2,1,1) 
plt.title("rk4 fric = 0.4")
plt.xlabel("t")
plt.ylabel("y0")
plt.plot(data[:,0],data[:,1])

plt.subplot(2,1,2) 
plt.title("Comparacion y0, y1")
plt.xlabel("y0")
plt.ylabel("y1")
plt.plot(data[:,1],data[:,2])

plt.savefig("rk4fric.png")