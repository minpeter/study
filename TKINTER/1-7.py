from tkinter import *

def calc(event):
    label.config(text="계산결과: " + str(eval(entry.get())))

root=Tk()
root.title("math")
root.geometry("300x200+100+100")
root.resizable(False, False)

label = Label(root, text="")
label.pack()

entry = Entry(root, width=30)
entry.bind("<Return>",calc)
entry.pack()

root.mainloop()