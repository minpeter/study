from tkinter import *

myid = "python"
mypw = "coding"

def slo(event):
	if(myid==entryid.get() and mypw==entrypw.get()):
		label.config(text = "로그인 되었습니다")
	else:
		label.config(text = "아이디 또는 패스워드 오류")

root=Tk()
root.title("ID PW")
root.geometry("300x200+100+100")
root.resizable(False, False)

entryid = Entry(root, width=30)
entryid.bind("<Return>",slo)
entryid.pack()

entrypw= Entry(root, width=30, show="*")
entrypw.bind("<Return>",slo)
entrypw.pack()

label = Label(root, text="")
label.pack()

root.mainloop()
