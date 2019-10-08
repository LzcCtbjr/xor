A tool to understand XOR better
===================
Why?
----------------

Originally, I found myself wondering about the XOR and what its effects on decimal numbers would be when applied bitwise to their binary values. I later shifted from just the XOR to other logical operators when I remembered that the XOR was just a composition of more basic operators. The goal of this is to be able to understand more fully what the bitwise logical operators do by looking at them through bases other than binary.  

What is each file?
----------------

xorTools.py provides all the mathematical backend that we'll be needing (finding the XOR given two decimal or binary numbers)

xorAnalyze.py generates a XOR table with user-specified dimensions, and then outputs this to the console and to 'output.txt'

-----------------
TODO:
-----------------------
1. find a better way to visualize the data, i.e. 3d graph with z = xor(x,y)
