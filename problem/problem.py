import tsv
from tkinter import *

root = Tk()

for row, row_list in enumerate(tsv.read_tsv):
    for column, value in enumerate(row_list): 
        myLabel = Label(root, text=value)
        myLabel.grid(row=row, column=column)

root.mainloop()
