#!/bin/python3

#list of methods:
#DectoBin(dec)
#HextoBin(hex)
#BintoDec(bin)
#xor(x,y)
#decXor(x,y)
#hexXor(x,y)

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

#####   BITWISE LOGIG METHODS   #####

def xor(x,y):
    #Finds the bitwise XOR by moving through the places and
    #putting a '1' in the output in that place if both bits
    #are different. If the iterating variable is outside the 
    #bounds of one of the numbers, it adds a '1' if the bit 
    #of the other string in that place is also a '1'
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

def bor(x,y):
    #Finds the bitwise OR by moving through the places and
    #putting a '1' if the bit in either string at that position
    #is also a '1'
    output = 0
    xlen = len(str(x))
    ylen = len(str(y))

    for i in range (1, max([xlen,ylen]) + 1):
        if i > xlen:
            output = output + int(str(y)[ylen - i]) * (10**(i-1))
        elif i > ylen:
            output = output + int(str(x)[xlen - i]) * (10**(i-1))
        elif int(str(x)[xlen - i]) ==  0 and int(str(y)[ylen - i]) == 0:
            output = output
        else:
            output = output + (10**(i-1))

    return output
       
def band(x,y):
    #Finds the bitwise AND by moving through the places and
    #putting a '1' if the bit in both strings at that position
    #is also a '1'
    output = 0
    xlen = len(str(x))
    ylen = len(str(y))

    for i in range (1, max([xlen,ylen]) + 1):
        if int(str(x)[xlen - i]) == int(str(y)[ylen - i]):
            output = output + (10**(i-1))

    return output

def bnot(x):
    #Finds the bitwise NOT by moving through the places and
    #flipping the bit found at each place
    output = int(x)
    for i in range (1, len(str(x)) + 1):
        output = output + ((10**(i-1)) * (1 - 2*int(str(x)[len(str(x)) - i])))
    return output
