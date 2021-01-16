import random
import time
from tkinter import Tk,Button,DISABLED


def show_sym(x,y):
    global f
    global px,py

    buttons[x,y]['text']=b_symbols[x,y]


    if f:
        px=x
        py=y
        f=False
        
    elif px!=x or py!=y:
        if buttons[px,py]['text'] != buttons[x,y]['text']:
            time.sleep(3)
            buttons[px,py]['text']=''
            buttons[x,y]['text']=''
        else:
            buttons[px,py]['command']=DISABLED
            buttons[x,y]['command']=DISABLED
        f = True
    else:
        buttons[px,py]['text']=''

win=Tk()
win.title('Matchmaker')
win.resizable(width=False,height=False)
f=True
px=0
py=0

buttons={}
b_symbols={}
symbol=[u'\u2702',u'\u2705',u'\u2708',u'\u2709',u'\u270A',u'\u270B',
            u'\u270C',u'\u270F',u'\u2712',u'\u2714',u'\u2716',u'\u2728',
            u'\u2702',u'\u2705',u'\u2708',u'\u2709',u'\u270A',u'\u270B',
            u'\u270C',u'\u270F',u'\u2712',u'\u2714',u'\u2716',u'\u2728']

random.shuffle(symbol)


for x in range(6):
    for y in range(4):
        bu=Button(command=lambda x=x,y=y: show_sym(x,y),width=10,height=8)
        bu.grid(column=x,row=y)
        buttons[x,y]=bu
        b_symbols[x,y]=symbol.pop()

win.mainloop()
