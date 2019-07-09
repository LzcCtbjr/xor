#!/bin/python3

def toBinary(x):
    return int(bin(x)[2:])

def toDecimal(x):
    output = 0
    for i in range (1,len(str(x)) + 1):
        if int(str(x)[len(str(x)) - i]) == 1:
            output = output + (2**(i-1))
    return output

def xor(x,y):
    output = 0
    xlen = len(str(x))
    ylen = len(str(y))

    for i in range (1,max([xlen,ylen]) + 1):
        if i > xlen:
            output = output + int(str(y)[ylen - i]) * (10**(i-1))
        elif i > ylen:
            output = output + int(str(x)[xlen - i]) * (10**(i-1))
        elif str(x)[xlen - i] != str(y)[ylen - i]:
            output = output + 1 * (10**(i-1))
    return output

def decXor(x,y):
    bin1 = str(toBinary(x))
    bin2 = str(toBinary(y))
    binxor = xor(bin1,bin2)
    return toDecimal(binxor)

'''
while True:
    in1 = int(input("Value one: "))
    bin1 = str(toBinary(in1))
    print("The binary is: " + bin1)

    in2 = int(input("Value two: "))
    bin2 = str(toBinary(in2))
    print("The binary is: " + bin2)

    binxor = xor(bin1,bin2)
    print("The XOR in binary is: " + str(binxor))
    print("The bitwise XOR in decimal is: " + str(toDecimal(binxor)))
'''
