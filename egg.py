from itertools import cycle
from random import randrange
from tkinter import *
from tkinter import messagebox



canvas_width=800
canvas_height=400

win=Tk()
c=Canvas(win,width=canvas_width,height=canvas_height,background='deep sky blue')
c.create_rectangle(-5,canvas_height-100,canvas_width+5,canvas_height+5,fill='sea green',width=0)
c.create_oval(-80,-80,120,120,fill='orange',width=0)

color_cycle=cycle(['light blue','light pink','red','blue','black','green','light yellow','light green'])
egg_w=45
egg_h=55
egg_s=10
egg_speed=500
egg_interval=4000
difficulty=0.95

catcher_color='black'
catcher_w=100
catcher_h=100
catcher_x1=canvas_width/2-catcher_w/2
catcher_y1=canvas_height-catcher_h-20
catcher_x2=catcher_x1+catcher_w
catcher_y2=catcher_y1+catcher_h

catcher=c.create_arc(catcher_x1,catcher_y1,catcher_x2,catcher_y2,start=200,extent=140,style='arc',outline=catcher_color,width=3)

score=0
score_txt=c.create_text(10,10,anchor='nw',font=('Arial',18,'bold'),fill='darkblue',text='Score :'+str(score))

lives=3
lives_txt=c.create_text(canvas_width-200,10,anchor='nw',font=('Arial',14,'bold'),fill='darkblue',text='lives remaining :'+str(lives))
c.pack()

eggs=[]

def create_egg():
    x=randrange(10,740)
    y=40
    new_egg=c.create_oval(x,y,x+egg_w,y+egg_h,fill=next(color_cycle),width=0)
    eggs.append(new_egg)
    win.after(egg_interval,create_egg)

def move_egg():
    for x in eggs:
        (x1,y1,x2,y2)=c.coords(x)
        c.move(x,0,10)
        if y2>canvas_height:
            egg_drop(x)
    win.after(egg_speed,move_egg)

def egg_drop(egg):
    eggs.remove(egg)
    c.delete(egg)
    lose_a_life()
    if lives==0:
        messagebox.showinfo('GAME OVER','FINAL SCORE :'+str(score))
        win.destroy()

def lose_a_life():
    global lives
    lives-=1
    c.itemconfigure(lives_txt,text='Lives :'+str(lives))

def catch():
    (x1,y1,x2,y2)=c.coords(catcher)
    for egg in eggs:
        (X1,Y1,X2,Y2)=c.coords(egg)
        if x1<X1 and X2<x2 and y2-Y2<40:
            eggs.remove(egg)
            c.delete(egg)
            inc_score(egg_s)
    win.after(100,catch)

def inc_score(points):
    global score,egg_speed,egg_interval
    score+=points
    egg_speed=int(egg_speed*difficulty)
    egg_interval=int(egg_interval*difficulty)
    c.itemconfigure(score_txt,text='Score :'+str(score))

def move_l(event):
    (x1,y1,x2,y2)=c.coords(catcher)
    if x1>0:
        c.move(catcher,-20,0)


def move_r(event):
    (x1,y1,x2,y2)=c.coords(catcher)
    if x2<canvas_width:
        c.move(catcher,20,0)

c.bind('<Left>',move_l)
c.bind('<Right>',move_r)
c.focus_set()

win.after(1000,create_egg)
win.after(1000,move_egg)
win.after(1000,catch)




win.mainloop()
