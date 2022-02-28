from tkinter import *

root = Tk()

def myClick():
	click_label = Label(root,text='I Clicked!!!')
	click_label.pack()

myButton = Button(root, text='Click Here', command=myClick)
myButton.pack()

root.mainloop()
