from tkinter import *

root = Tk()

def myClick():
	click_label = Label(root,text=e.get( ))
	click_label.pack()

def del_txt():
	e.delete(0,len(e.get()))

def in_txt(x):
	e.insert(len(e.get()),x*'vrau')

e = Entry(root, width=90)
e.pack()
e.insert(0,'Enter your name')

myButton = Button(root, text='Click Here', command=myClick)
bd=Button(root,text='Clear',command=del_txt).pack()
bi=Button(root,text='insert_vrau',command=lambda: in_txt(2)).pack()
myButton.pack()

root.mainloop()
