from tkinter import Tk,HIDDEN,NORMAL,Canvas


def toggle_eyes():
    current_color=c.itemcget(eye_left,'fill')
    new_color=c.body_color if current_color=='white' else 'white'
    current_state=c.itemcget(t_left,'state')
    new_state =NORMAL if current_state==HIDDEN else HIDDEN
    c.itemconfigure(t_left,state=new_state)
    c.itemconfigure(t_right,state=new_state)
    c.itemconfigure(eye_left, fill=new_color)
    c.itemconfigure(eye_right, fill=new_color)

def blink():
    toggle_eyes()
    win.after(250,toggle_eyes)
    win.after(2000,blink)

def t_pupils():
    if not c.cro_eyes:
        c.move(t_left,10,-5)
        c.move(t_right,-10,-5)
        c.cro_eyes=True
    else:
        c.move(t_left,-10,5)
        c.move(t_right,10,5)
        c.cro_eyes=False

def t_tounge():
    if not c.tou_out:
        c.itemconfigure(tounge_tip, state=NORMAL)
        c.itemconfigure(tounge_main, state=NORMAL)
        c.tou_out=True
    else:
        c.itemconfigure(tounge_tip, state=HIDDEN)
        c.itemconfigure(tounge_main, state=HIDDEN)
        c.tou_out=False

def cheeky(event):
    t_tounge()
    c.itemconfigure(mouth_normal,state=HIDDEN)
    t_pupils()
    hide_happy(event)
    c.itemconfigure(guess,state=HIDDEN)
    c.itemconfigure(guess1,state=HIDDEN)
    win.after(1000,t_tounge)
    win.after(1000,t_pupils)
    c.itemconfigure(thanks,state=NORMAL)

    return

def happy(event):
    if(20<= event.x and event.x<=350) and (20<=event.y and event.y<=350):
        c.itemconfigure(c_left,state=NORMAL)
        c.itemconfigure(c_right,state=NORMAL)
        c.itemconfigure(mouth_happy,state=NORMAL)
        c.itemconfigure(mouth_normal,state=HIDDEN)
        c.itemconfigure(mouth_sad,state=HIDDEN)
        c.happy_lvl=8
        return

def hide_happy(event):
    c.itemconfigure(c_left,state=HIDDEN)
    c.itemconfigure(c_right,state=HIDDEN)
    c.itemconfigure(mouth_happy,state=HIDDEN)
    c.itemconfigure(mouth_normal,state=NORMAL)
    c.itemconfigure(mouth_sad,state=HIDDEN)
    return

def sad():
    if c.happy_lvl==0:
        c.itemconfigure(mouth_happy,state=HIDDEN)
        c.itemconfigure(mouth_normal,state=HIDDEN)
        c.itemconfigure(mouth_sad,state=NORMAL)
        c.itemconfigure(thanks,state=HIDDEN)
        c.itemconfigure(guess,state=NORMAL)
        c.itemconfigure(guess1,state=NORMAL)

    else:
        c.happy_lvl-=1
        print(c.happy_lvl)
    win.after(500,sad)




win=Tk()

c=Canvas(win, width=400, height=400)
c.configure(bg='dark blue', highlightthickness=0)

c.body_color='SkyBlue1'

guess=c.create_text(200,370,fill="black",font="italic 20",
                        text="Pet me please",state=HIDDEN)
guess1=c.create_text(200,390,fill="black",font="italic 10",
                        text="by double clicking",state=HIDDEN)
thanks=c.create_text(200,370,fill="black",font="italic 20",
                        text="Thanks sooo much :)",state=HIDDEN)

body= c.create_oval(35,20,365,350,outline=c.body_color,fill=c.body_color)
foot_l=c.create_oval(65,320,145,360,outline=c.body_color,fill=c.body_color)
foot_r=c.create_oval(250,320,330,360,outline=c.body_color,fill=c.body_color)


ear_left=c.create_polygon(75,80,75,10,165,70,outline=c.body_color,fill=c.body_color)
ear_left=c.create_polygon(225,45,325,10,320,70,outline=c.body_color,fill=c.body_color)

eye_left=c.create_oval(130,110,160,170,outline='black',fill='white')
t_left=c.create_oval(140,145,150,155,outline='black',fill='black')

eye_right=c.create_oval(230,110,260,170,outline='black',fill='white')
t_right=c.create_oval(240,145,250,155,outline='black',fill='black')


mouth_normal=c.create_line(170,250,200,272,230,250,smooth=1,width=2,state=NORMAL)
mouth_happy=c.create_line(170,250,200,282,230,250,smooth=1,width=2,state=HIDDEN)
mouth_sad=c.create_line(170,250,200,232,230,250,smooth=1,width=2,state=HIDDEN)

tounge_main=c.create_rectangle(180,250,220,290,outline='red',fill='red',state=HIDDEN)
tounge_tip=c.create_oval(180,285,220,300,outline='red',fill='red',state=HIDDEN)

c_left=c.create_oval(70,180,120,230,outline='pink',fill='pink',state=HIDDEN)
c_right=c.create_oval(280,180,330,230,outline='pink',fill='pink',state=HIDDEN)

c.pack()

c.bind('<Motion>',happy)
c.bind('<Leave>',hide_happy)
c.bind('<Double-1>',cheeky)

win.after(1000,blink)
win.after(5000,sad)



c.cro_eyes=False
c.tou_out=False
c.happy_lvl=0


win.mainloop()
