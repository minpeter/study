from tkinter import *

def fplus():
    label.config(text="계산결과: " + str(int(entry1.get()) + int(entry2.get())))

def fminus():
    label.config(text="계산결과: " + str(int(entry1.get()) - int(entry2.get())))

def fmultiply():
    label.config(text="계산결과: " + str(int(entry1.get()) * int(entry2.get())))

def fdivision():
    label.config(text="계산결과: " + str(int(entry1.get()) / int(entry2.get())))

root=Tk()
root.title("math")
root.geometry("300x230+100+100")
root.resizable(False, False)

entry1 = Entry(root, width=30)
entry1.pack()

entry2 = Entry(root, width=30)
entry2.pack()

plus = Button(root,text="+",width=10,relief="solid",command=fplus)
plus.pack()

minus = Button(root,text="-",width=10,relief="solid",command=fminus)
minus.pack()

multiply = Button(root,text="*",width=10,relief="solid",command=fmultiply)
multiply.pack()

division = Button(root,text="/",width=10,relief="solid",command=fdivision)
division.pack()

label = Label(root, text="")
label.pack()

root.mainloop()
