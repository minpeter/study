from tkinter import *

root=Tk()

root.title("info")
root.geometry("300x200+100+100")
root.resizable(False, False)

name = Label(root, text='민웅기')
name.pack()

school = Label(root, text='장기중학교')
school.pack()

call = Label(root, text='010-3177-4371')
call.pack()


root.mainloop()