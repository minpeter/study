from tkinter import *

root=Tk()


def fname():
    label.config(text="민웅기")

def fschool():
    label.config(text="장기중학교")

def fcall():
    label.config(text="010-3177-4371")

root.title("info")
root.geometry("300x200+100+100")
root.resizable(False, False)

label = Label(root, text=" ")
label.pack()

name = Button(root,text="이름",width=10,relief="solid",command=fname)
name.pack()

school = Button(root,text="학교",width=10,relief="solid",command=fschool)
school.pack()

call = Button(root,text="전화번호",width=10,relief="solid",command=fcall)
call.pack()

root.mainloop()