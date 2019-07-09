#!/usr/bin/python3
from xorTools import *
import matplotlib.pyplot as plt

w = 25
h = 25
arr = [[0 for x in range(w)] for y in range(h)]

for i in range(0, w):
    for j in range(0,h):
        arr[i][j] = decXor(i,j)

table = plt.table(cellText=arr,
                    rowLabels=arr[0][:],
                    colLabels=arr[:][0],
                    loc='top')

plt.show()
