from tkinter import *

def slo(event):
	if int(number.get())>=0 and int(number.get())<=30:
		label.config(text = "좋음", fg="green")
	elif int(number.get())>=31 and int(number.get())<=80:
		label.config(text = "보통", fg="blue")
	elif int(number.get())>=81 and int(number.get())<=150:
		label.config(text = "나쁨", fg="orange")
	elif int(number.get())>=151:
		label.config(text = "매우나쁨", fg="red")
	

root = Tk()
root.title("미세먼지")
root.geometry("300x200+100+100")
root.resizable(False,False)

number = Entry(root, width=30)
number.bind("<Return>", slo)
number.pack()

label = Label(root, text="",fg="red")
label.pack()

root.mainloop()
