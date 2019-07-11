#!/bin/python3

#####   IMPORTS LIBRARIES   #####

import pyglet
from pyglet.window import key
from xorTools import *

#####   GETS EVERYTHING READY   #####

#initial values for inputs
x = 1
y = 1
#constants for rendering
fontName = 'Times New Roman'
fontSize = 18

#creates the window object
window = pyglet.window.Window()

#####   DEFINES THE METHODS THAT WE'LL NEED #####

#the math backend for this, we call this each time we update the values
def calc():
    binX = DectoBin(x)
    binY = DectoBin(y)
    out = xor(binX,binY)
    return [binX, binY, out]

#method for creating all the labels
def generate(x, y):
    vars = calc()

    xLabel = pyglet.text.Label(str(x),
                                font_name = fontName,
                                font_size = fontSize,
                                x=window.width//100, y=window.height//2,
                                anchor_x='left', anchor_y='center')
    yLabel = pyglet.text.Label(str(y),
                                font_name = fontName,
                                font_size = fontSize,
                                x=window.width//2, y=9*window.height//10,
                                anchor_x='center', anchor_y='center')
    binXLabel = pyglet.text.Label(str(vars[0]),
                                font_name = fontName,
                                font_size = fontSize*2,
                                x=window.width//100, y=(window.height//2) - fontSize * 1.5,
                                anchor_x='left', anchor_y='center')
    binYLabel = pyglet.text.Label(str(vars[1]),
                                font_name = fontName,
                                font_size = fontSize*2,
                                x=window.width//2, y=(99*window.height//100) - fontSize * 4,
                                anchor_x='left', anchor_y='center')
    xorLabel = pyglet.text.Label(str(vars[2]),
                                font_name = fontName,
                                font_size = fontSize*2,
                                x=window.width//2, y=window.height//2 - fontSize * 1.5,
                                anchor_x='left', anchor_y='center')
    return [xLabel, yLabel, binXLabel, binYLabel, xorLabel]

#####   RENDERING   #####

@window.event
#what to do when the window is drawn for the first time
def on_draw():
    window.clear()
    labels = generate(x,y)
    for i in range(len(labels)):
        labels[i].draw()

@window.event
#defines what to do on certain keypresses
def on_key_press(symbol, modifiers):
    global x,y
    if symbol == key.Q:
        exit()
    elif symbol == key.H:
        x = x - 1
        if x < 0:
            x = 0
    elif symbol == key.L:
        x = x + 1
    elif symbol == key.J:
        y = y - 1
        if y < 0:
            y = 0
    elif symbol == key.K:
        y = y + 1
    on_draw()

#runs the application
pyglet.app.run()
