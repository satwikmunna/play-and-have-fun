import turtle as t
import random as rd
import time as ti



def inside():
    left_limit=(-t.window_width()/2)+100
    right_limit=(t.window_width()/2)-100
    up_limit=(t.window_width()/2)-100
    bottom_limit=(-t.window_width()/2)+100
    (x,y)=t.pos()
    inside=left_limit<x<right_limit and bottom_limit<y<up_limit
    return inside



def move():
    if inside():
        angle=rd.randint(0,100)
        dist=rd.randint(50,300)
        t.right(dist)
        t.forward(200)
    else:
        t.backward(200)


t.shape('turtle')
t.fillcolor('green')
t.bgcolor('black')
t.speed('fast')


while True:
    move()










ti.sleep(3)
