A tool to understand XOR better
===================
Why?
----------------

I was reading about the bitwise XOR and I found myself wondering what the effects of it would be on numbers in other bases, so I made this tool to help look at how numbers act with it.

What is each file?
----------------

xorTools.py provides all the mathematical backend that we'll be needing (finding the XOR given two decimal or binary numbers)

xorAnalyze.py generates a XOR table with user-specified dimensions, and then outputs this to the console and to 'output.txt'

xorPeek.py is an interactive tool to change each input and see what the resulting XOR is in both binary and decimal 

TODO:
-----------------------
1. keep thinking about whether there's a better way to structure the programs
2. find a better way to visualize the data, i.e. 3d graph with z = xor(x,y)
