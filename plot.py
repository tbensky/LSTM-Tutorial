import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt('data.csv', delimiter=',')

t = []
y1 = []
y2 = []
y3 = []
y4 = []

for line in data:
    if line[0] < 100:
        t.append(line[0])
        y1.append(line[1])
        y2.append(line[1+4])
        y3.append(line[1+4+4])
        y4.append(line[1+4+4+4])

plt.subplot(4,1,1)
plt.plot(t,y1,'.')
plt.ylabel("x")
plt.title("Particle 0")



plt.subplot(4,1,2)
plt.plot(t,y2,'.')
plt.ylabel("x")
plt.title("Particle 1")


plt.subplot(4,1,3)
plt.plot(t,y3,'.')
plt.ylabel("x")
plt.title("Particle 2")

plt.subplot(4,1,4)
plt.plot(t,y4,'.')
plt.ylabel("x")
plt.title("Particle 3")

plt.tight_layout()
plt.xlabel("Time")

plt.savefig("sample.png",dpi=300)
plt.close()