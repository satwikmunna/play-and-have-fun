from tkinter import *

def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    return a / b

def mod(a,b):
    return a % b

def lcm(a,b):
    L = a if a>b else b
    while L <= a*b:
        if L%a == 0 and L%b == 0:
            return L
        L+=1

def hcf(a,b):
    H = a if a<b else b
    while H >= 1:
        if a%H == 0 and b%H == 0:
            return H
        H-=1



def ex_txt(text):
    l=[]
    for t in text.split(' '):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return l



def cal():
    text=textin.get()
    for w in text.split(' '):
        if w.upper() in operations.keys():
            try:
                l=ex_txt(text)
            
                r=operations[w.upper()](l[0],l[1])
                list.delete(0,END)
                list.insert(END,r)
            except:
                list.delete(0,END)
                list.insert(END,'something wrong')
            finally:
                break
        elif w.upper() not in operations.keys():
            list.delete(0,END)
            list.insert(END,'something wrong elif')


operations = {'ADD':add , 'ADDITION':add , 'SUM':add , 'PLUS':add ,
                'SUB':sub , 'DIFFERENCE':sub , 'MINUS':sub , 'SUBTRACT':sub,
                 'LCM':lcm , 'HCF':hcf , 'PRODUCT':mul , 'MULTIPLICATION':mul,
                 'MULTIPLY':mul , 'DIVISION':div , 'DIV':div ,'DIVIDE':div, 'MOD':mod ,
                  'REMANDER':mod , 'MODULUS':mod}

win=Tk()
win.geometry("500x300")
win.title("Smart Madam")
win.configure(bg='lightskyblue')



l1=Label(win,text="i am a smart calculator",width=20,padx=15)
l1.place(x=150,y=10)
l2=Label(win,text="My name is Madam",padx=10)
l2.place(x=180,y=40)
l1=Label(win,text="what can i do for u",padx=10)
l1.place(x=176,y=130)



textin=StringVar()
e1=Entry(win,width=40,textvariable=textin)
e1.place(x=150,y=160)

b1=Button(win,text="Go",command=cal)
b1.place(x=230,y=200)


list=Listbox(win,width=30,height=3)
list.place(x=150,y=230)

win.mainloop()
