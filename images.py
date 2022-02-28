from tkinter import *
#
root=Tk()
root.title('Test Title')
root.iconbitmap(r"..\..\..\Pictures\Saved Pictures\test_icon.ico")
#
bq=Button(root, text='bye', command=root.quit)
bq.pack()
#
root.mainloop()
