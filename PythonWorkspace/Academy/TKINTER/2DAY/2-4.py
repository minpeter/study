from tkinter import *

def slo(event):
	for i in range(len(ll)):
		ll[i].config(text=str(entry.get()) + " x " + str(i+2) + " = " + str(int(entry.get())*i+2))

root = Tk()
root.title("구구단")
root.geometry("300x250+100+100")
root.resizable(False,False)

entry = Entry(root, width=30)
entry.bind("<Return>",slo)
entry.pack()

ll=[]

for i in range(8):
	label = Label(root)
	label.pack()
	ll.append(label)

root.mainloop()
