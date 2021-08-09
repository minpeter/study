from tkinter import *

root=Tk()

root.title("bitmap")
root.geometry("300x200+100+100")
root.resizable(False, False)

info = Label(root, text='정보', width=100,height=50, bitmap="info", compound="top")
info.pack()

error = Label(root, text='에러', width=100,height=50, bitmap="error", compound="top")
error.pack()

hourglass = Label(root, text='로딩중', width=100,height=50,bitmap="hourglass", compound="top")
hourglass.pack()


root.mainloop()