import numpy as np

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

with open('dataset.dat', 'w') as data:
    for i in range(100):
        n = int(np.random.uniform(1, 3))
        data.write(str(n) + ' : ')
        if n == 1:
            for i in range(1000):
                point = generate1()
                data.write(str(point[0]) + ' ' + str(point[1]) + ' ')
        else:
            for i in range(1000):
                point = generate2()
                data.write(str(point[0]) + ' ' + str(point[1]) + ' ')
        data.write('\n')
