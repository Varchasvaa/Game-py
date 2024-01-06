from tkinter import*
import random as rn

win=Tk()
win.geometry('600x500')
win.title('Varchasva')

la=Label(win,text="Dont Click it ",font=10)
la.place(x=250,y=0)

cl=Label(win,text='colours',font=10)
cl.place(x=0,y=0)

p=Label(win,text="0",font='10')
p.place(x=500,y=0)

time=Label(win,text='0',font='10')
time.place(x=450,y=0)

b=Button(win,text='Bye',fg='red',command=win.destroy)
b.place(x=550,y=450)
colour=['maroon','yellow','orange','purple','cyan']
colours=['magenta','red','pink','blue','green']

def click():
#        win.configure(bg='grey')
#         cl.configure(bg='grey')
#         p.configure(bg='grey')
#         la.configure(bg='grey')
        la.configure(text='U did it')
        p.configure(text=str(int(p.cget('text'))+1))
        color=rn. choice(colour)
        colors=rn. choice(colours)
        cl.configure(text=color,fg=color,bg=colors)
        c.configure(text='Click',fg=color,bg=colors)
        c.place(x=rn.randint(10,450),y=rn.randint(10,400))
        f.configure(text='Click',fg=rn. choice(colours),bg=rn. choice(colour))
        f1.configure(text='Click',fg=rn. choice(colours),bg=rn. choice(colour))
        f2.configure(text='Click',fg=rn. choice(colours),bg=rn. choice(colour))
        f3.configure(text='Click',fg=rn. choice(colours),bg=rn. choice(colour))
        f.place(x=rn.randint(10,450),y=rn.randint(10,400))
        f1.place(x=rn.randint(10,450),y=rn.randint(10,400))
        f2.place(x=rn.randint(10,450),y=rn.randint(10,400))
        f3.place(x=rn.randint(10,450),y=rn.randint(10,400))
def oop():
        la.place(x=270,y=250)
        la.configure(text='U failed ')
        f.configure(text='Click')
        c.after(1000,lambda:win.destroy())
              
c=Button(win,text="Start",fg='purple',command=click)
c.place(x=250,y=100)
f=Button(win,text="Start",fg='magenta',command=oop)
f.place(x=10000,y=0)
f1=Button(win,text="Start",fg='magenta',command=oop)
f1.place(x=10000,y=0)
f2=Button(win,text="Start",fg='magenta',command=oop)
f2.place(x=10000,y=0)
f3=Button(win,text="Start",fg='magenta',command=oop)
f3.place(x=10000,y=0)
win.mainloop()