#!/usr/bin/python3

from xorTools import *
from tabulate import tabulate
import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

print("-----xorAnalyze-----")
print("[1] AND")
print("[2] OR")
print("[3] XOR")
mode = int(input('Mode: '))

w = int(input('hrange: '))
h = int(input('vrange: '))

arr = [[0 for y in range(h)] for x in range(w)]

for i in range(0, w):
    for j in range(0,h):
        if mode == 1:
            arr[i][j] = BintoDec(band(DectoBin(i), DectoBin(j)))
        elif mode == 2:
            arr[i][j] = BintoDec(bor(DectoBin(i),DectoBin(j)))
        elif mode == 3:
            arr[i][j] = BintoDec(xor(DectoBin(i),DectoBin(j)))

with open('output.txt', 'w') as f:
    print(tabulate(arr))
    f.write(tabulate(arr))

print("-----Display-----")
print("[1] 3D graph")

mode = int(input('Mode: '))
if mode == 1:
    x = [i for i in range(w)]
    y = [i for i in range(h)]

    X, Y = np.meshgrid(x,y)
    Z = arr

    fig = plt.figure
    ax = plt.axes(projection='3d')
    ax.scatter3D(X, Y, Z)
    plt.show()
