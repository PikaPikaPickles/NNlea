import numpy as np

def get_set():
    with open("dataset.dat") as data:
        s = data.readline()
    correct_ans = int(s[0]) - 1
    s = s[4 : len(s)]
    s = list(map(float, s.split()))
    res = np.array([s[::2], s[1::2]])
    return correct_ans, res
