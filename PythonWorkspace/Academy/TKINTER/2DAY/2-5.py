from tkinter import *

def slo():
	label.config(text="나는 " + listbox.get(listbox.curselection()[0]) + "를 좋아해")

root=Tk()
root.title("과일")
root.geometry("300x200+100+100")
root.resizable(False, False)

fruits = ['사과','수박','딸기','귤']

listbox = Listbox(root, height=0, selectmode = "browse")

for i in range(len(fruits)):
	listbox.insert(i,fruits[i])

listbox.pack()

button = Button(root, width=20, text="like", command=slo)
button.pack()

label = Label(root, text="")
label.pack()

root.mainloop()
