from tkinter import *

root = Tk()
root.geometry("400x300")
root.title("Main")

def topwin():
    top = Toplevel()
    top.geomtry("100x100")

    l2 = Label(top, text = "Thsi is top level window")
    l2.pacl()

    top.mainloop()

l = Label(root,text = " This is root window")
btn = Button(root, text ="click here to open another window ",command = topwin)

l.pack()
btn.pack()

root.mainloop()