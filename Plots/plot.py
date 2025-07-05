import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt('../data.csv', delimiter=',')

N = 25
t = []
y = []
for p in range(N):
    y.append([])

for line in data:
    if line[0] < 100:
        t.append(line[0])
        for p in range(N):
            y[p].append(line[1+p*4])

for p in range(N):
    plt.plot(t,y[p],'.')
    plt.ylabel("x")
    plt.xlabel("Time")
    plt.title(f"Particle {p}")
    plt.savefig(f"p{p}.png",dpi=300)
    plt.close()

