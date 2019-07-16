A tool to understand XOR better
===================
Why?
----------------

Originally, I found myself wondering about the XOR and what its effects on decimal numbers would be when applied bitwise to their binary values. I later shifted from just the XOR to other logical operators when I remembered that the XOR was just a composition of more basic operators. The goal of this is to be able to understand more fully what the bitwise logical operators do by looking at them through bases other than binary.  

What is each file?
----------------

xorTools.py provides all the mathematical backend that we'll be needing (finding the XOR given two decimal or binary numbers)

xorAnalyze.py generates a XOR table with user-specified dimensions, and then outputs this to the console and to 'output.txt'

xorPeek.py is an interactive tool to change each input and see what the resulting XOR is in both binary and decimal 

Notes:
-----------------

My definition of the NOT on decimals is somewhat confusing (and very much not finalized) and needs some explanation.

My implementation of NOT is different from how a computer treats this samebitwise operation. For example, python's bitwise NOT returns the complement of x, which for computers is the same as -1 * (x + 1).
[Python used to use numbers with a word length of however many bits were native to what it was running on, but now uses numbers with an "infinite" amount of bits. This means that the number '-5' would be treated as if it were "...11111111111111011".](https://wiki.python.org/moin/BitwiseOperators)

From a mathematician's perspective, however, this does not make sense. If we treat binary like just a different base and remove it from how computers store numbers, there is no 'negative place value', and Python's '-5' would just be infinity. Furthermore, math assumes an infinite amount of preceeding '0's before every number, meaning that the NOT of anything would just return an infinite number.

Because of this, my definition of NOT deals with these issues by disregarding word length and negative numbers, and truncating all preceeding zeros. Because zero is a special case, I have decided to make NOT(0) DNE. I'm still slightly unsure about the NOT of zero, so this might change moving forwards.

TODO:
-----------------------
1. expand peek to also allow for using the other bitwise logic operations on decimal numbers
2. find a better way to visualize the data, i.e. 3d graph with z = xor(x,y)
3. consider removing the methods to deal with hex numbers (is understanding decimal enough? is understanding decimal sufficient to understand the hex without additional research?)
