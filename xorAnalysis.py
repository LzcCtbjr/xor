#!/usr/bin/python3
from xorTools import *
from tabulate import tabulate

w = 25
h = 25
arr = [[0 for x in range(w)] for y in range(h)]

for i in range(0, w):
    for j in range(0,h):
        arr[i][j] = decXor(i,j)

with open('output.txt', 'w') as f:
    print(tabulate(arr))
    f.write(tabulate(arr))
