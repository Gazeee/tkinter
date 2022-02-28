from tkinter import *

root = Tk()

def myClick():
	click_label = Label(root,text=e.get( ))
	click_label.pack()

e = Entry(root, width=90)
e.pack()
e.insert(0,'Enter your name')

myButton = Button(root, text='Click Here', command=myClick)
myButton.pack()

root.mainloop()
