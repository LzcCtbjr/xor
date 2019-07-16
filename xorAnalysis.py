#!/usr/bin/python3
from xorTools import *
from tabulate import tabulate

print("-----xorAnalyze-----")
print("[1] AND")
print("[2] OR")
print("[3] NOT")
print("[4] XOR")
mode = int(input('Mode: '))

if mode != 3:
    w = int(input('hrange: '))
    h = int(input('vrange: '))
else:
    h = int(input('hrange: '))
    w = 1

arr = [[0 for y in range(h)] for x in range(w)]

for i in range(0, w):
    for j in range(0,h):
        if mode == 1:
            arr[i][j] = BintoDec(band(DectoBin(i), DectoBin(j)))
        elif mode == 2:
            arr[i][j] = BintoDec(bor(DectoBin(i),DectoBin(j)))
        elif mode == 3:
            if bnot(DectoBin(j)) is not None:
                arr[i][j] = BintoDec(bnot(DectoBin(j)))
        elif mode == 4:
            arr[i][j] = BintoDec(xor(DectoBin(i),DectoBin(j)))

with open('output.txt', 'w') as f:
    print(tabulate(arr))
    f.write(tabulate(arr))
