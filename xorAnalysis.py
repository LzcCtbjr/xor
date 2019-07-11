#!/usr/bin/python3
from xorTools import *
from tabulate import tabulate

w = int(input('hrange: '))
h = int(input('vrange: '))

arr = [[0 for y in range(w)] for x in range(h)]

for i in range(0, h):
    for j in range(0,w):
        arr[i][j] = decXor(i,j)

with open('output.txt', 'w') as f:
    print(tabulate(arr))
    f.write(tabulate(arr))
