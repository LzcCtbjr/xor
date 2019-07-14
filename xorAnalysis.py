#!/usr/bin/python3
from xorTools import *
from tabulate import tabulate

print("-----xorAnalyze-----")
print("[1] AND")
print("[2] OR")
print("[3] XOR")
mode = int(input('Mode: '))

w = int(input('hrange: '))
h = int(input('vrange: '))

arr = [[0 for y in range(w)] for x in range(h)]

for i in range(0, h):
    for j in range(0,w):
        if mode == 1:
            arr[i][j] = BintoDec(band(DectoBin(i), DectoBin(j)))
        elif mode == 2:
            arr[i][j] = BintoDec(bor(DectoBin(i),DectoBin(j)))
        elif mode == 3:
            arr[i][j] = BintoDec(xor(DectoBin(i),DectoBin(j)))

with open('output.txt', 'w') as f:
    print(tabulate(arr))
    f.write(tabulate(arr))
