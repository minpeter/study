from tkinter import *
msg = ""

def rt(event):
    global msg
    msg = msg + entry.get() + "\n"
    label.config(text=msg)

root=Tk()
root.title("메아리")
root.geometry("300x200+100+100")
root.resizable(False, False)

entry = Entry(root, width=30)
entry.bind("<Return>",rt)
entry.pack()

label = Label(root, text="")
label.pack()

root.mainloop()