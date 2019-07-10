#!/bin/python3

#####   toBin METHODS   #####
#kinda self explanatory; just uses the builtin
#int() and bin() methods to convert to binary.
#the [2:] is to get rid of the '0x' that would
#be present because of how int() and bin() work.

def DectoBin(x):
    return bin(x)[2:]

def HextoBin(x):
    return bin(int(x,16))[2:]

#####   Binto METHODS   #####
#Uses builtin methods to undo the work done by 
#the toBin methods.

def BintoDec(x):
    #I really don't know why the commented return
    #statement doesn't work as intended, so I'm just
    #using a simple algorithm to convert to decimal.
    #return int(x,2)[2:]
    output = 0
    for i in range (1,len(str(x)) + 1):
        if int(str(x)[len(str(x)) - i]) == 1:
            output = output + (2**(i-1))
    return output

def BintoHex(x):
    return hex(int(x,2))[2:]

#####   BITWISE XOR METHOD  #####
#Finds the bitwise XOR by moving through the places and
#putting a '1' in the output in that place if both bits
#are different. If the iterating variable is outside the 
#bounds of one of the numbers, it adds a '1' if the bit 
#of the other string in that place is also a '1'

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

#####   "DO EVERYTHING FOR YOU" METHODS #####
#The general scheme for these methods is almost identical,
#with only the methods used to change bases being different
#between them. They:
#   1. Convert their inputs to binary
#   2. Find the bitwise XOR of the inputs
#   3. Convert the XOR back to the original base

def decXor(x,y):
    bin1 = str(DectoBin(x))
    bin2 = str(DectoBin(y))
    binxor = xor(bin1,bin2)
    return BintoDec(binxor)

def hexXor(x,y):
    bin1 = str(HextoBin(x))
    bin2 = str(DectoBin(y))
    binxor = xor(bin1,bin2)
    return BintoHex(binxor)
