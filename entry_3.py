from tkinter import *

root = Tk()

def f(x):
	Label(root,text=x).grid(row=8,column=5)
	#entrada.delete(0,len(entrada.get()))

entrada=Entry(root,width=100,borderwidth=5)
entrada.grid(row=4,column=4,columnspan=3)
b_1=Button(root, text='Separete', padx=15, pady=10,command=lambda: f(entrada.get())).grid(row=6,column=5)

root.mainloop()
