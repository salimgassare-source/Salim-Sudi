from tkinter import*

w = Tk()
w.geometry("800x500")
w.title("PYTHON GUI PROGRAMMING")

mainScreen= Label(w, text="MAIN SCREEN DISPLAY", fg= "blue")
mainScreen.grid(row=3,column=0)

screen= Entry(w)
screen.grid(row=3, column=1)

firstNumber= Label(w, text="First Number")
firstNumber.grid(row=0,column=0)

firstEntry = Entry(w)
firstEntry.grid(row=0,column=1)

secondNumber = Label(w, text="Second Number")
secondNumber.grid(row=1,column=0)

secondEntry= Entry(w)
secondEntry.grid(row=1,column=1)

def Add():
    a=int(firstEntry.get())
    b=int(secondEntry.get())
    sum=a+b
    screen.insert(0,sum)

b=Button(w, text= "ADD",fg="brown", command=Add)
b.grid(row=2, column =0)


w.mainloop()