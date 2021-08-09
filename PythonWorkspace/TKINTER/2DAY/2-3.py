from tkinter import *

def slo():
	label.config(text=str(entry1.get())+"님에게 "+str(entry2.get())+"라고 문자를 보냈습니다")
root = Tk()
root.title("메세지")
root.geometry("300x200+100+100")
root.resizable(False,False)

entry1 = Entry(root, width=30)
entry1.pack()

entry2 = Entry(root, width=30)
entry2.pack()

button = Button(root, width=30, text="전송", command=slo)
button.pack()

label = Label(root, text="")
label.pack()

root.mainloop()
