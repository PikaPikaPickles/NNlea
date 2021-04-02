import numpy as np
import matplotlib.pyplot as plt

def generate1():
    a = np.random.uniform(0, 1)
    b = np.random.uniform(0, 1)
    return (a * np.cos(2 * np.pi * b), a * np.sin(2 * np.pi * b))

def generate2():
    while True:
        x = np.random.uniform(-1, 1)
        y = np.random.uniform(-1, 1)
        if x ** 2 + y ** 2 > 1:
            continue
        return (x, y)

gen1 = [generate1() for i in range(1000)]
gen2 = [generate2() for i in range(1000)]
x1 = [i[0] for i in gen1]
y1 = [i[1] for i in gen1]
x2 = [i[0] for i in gen2]
y2 = [i[1] for i in gen2]

fig, ax = plt.subplots(1, 2)
ax[0].scatter(x1, y1)
ax[1].scatter(x2, y2, color='red')
ax[0].set_aspect('equal')
ax[1].set_aspect('equal')
ax[0].grid()
ax[1].grid()
plt.show()

