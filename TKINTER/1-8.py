from tkinter import *

root = Tk()
root.title("파이썬")
root.geometry("300x200+100+100")
root.resizable(False,False)

listbox = Listbox(root, height=0,selectmode="browse")
listbox.insert(0,"국어")
listbox.insert(0,"영어")
listbox.insert(0,"수학")
listbox.insert(0,"과학")
listbox.pack()

root.mainloop()