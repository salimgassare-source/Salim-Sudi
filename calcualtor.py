from tkinter import*

w=Tk()
w.title("GASSARES CALCULATOR")
w.geometry("800x500")

display=Entry(w, width=26,bg='black',fg='white', font=('Lucida Fax', 20))
display.grid(row=0,column=0, columnspan=4, padx=10, pady=10)

#main function: displaying the entered value
global n
def number(n):
    a =display.get()
    display.delete(0,END)
    display.insert(0,str(a)+str(n))
    
 #saving the first number   
def operation(op):
    try:
        global operator
        operator =op
        global firstNumber
        firstNumber=int(display.get())
  
        display.insert(0,str(firstNumber)+str(operator))
        display.delete(0,END)

    except ValueError:
        y ='Enter values first !'
        display.insert(0,y)
       
#saving the second number and adding it to the first number then displaying the sum
def eql():
    try:
        global secondNumber
    
        secondNumber=int(display.get())
        display.insert(0,str(secondNumber))
        display.delete(0,END)
  
        answer=display.get()

        match operator:
            case '+':
                answer=firstNumber+secondNumber

            case '-':
                answer=firstNumber-secondNumber

            case '÷':
                answer=firstNumber/secondNumber

            case '×':
                answer=firstNumber*secondNumber

           
    except ValueError:
        y ='Enter values first !'
        display.insert(0,y)
     
    else:
        display.insert(0,str(firstNumber) +str(' ')+ str(operator)+str(' ') +str(secondNumber)+str(' = ')+str(answer)) 
   

def clear():
    display.delete(0,END)

b1=Button(w, text=1, width=5, height=1, font=('Lucida Fax',20), bg='gray', command=lambda:number(1))
b1.grid(row=1,column=0)

b2=Button(w, text=2, width=5, height=1,font=('Lucida Fax',20), bg='gray', command=lambda:number(2))
b2.grid(row=1,column=1)

b3=Button(w, text=3, width=5, height=1, font=('Lucida Fax',20), bg='gray', command=lambda:number(3))
b3.grid(row=1,column=2)

b4=Button(w, text=4, width=5, height=1,font=('Lucida Fax',20), bg='gray', command=lambda:number(4))
b4.grid(row=1,column=3)

b5=Button(w, text=5, width=5, height=1, font=('Lucida Fax',20), bg='gray', command=lambda:number(5))
b5.grid(row=2,column=0)

b6=Button(w, text=6, width=5, height=1, font=('Lucida Fax',20), bg='gray', command=lambda:number(6))
b6.grid(row=2,column=1)

b7=Button(w, text=7, width=5, height=1, font=('Lucida Fax',20), bg='gray', command=lambda:number(7))
b7.grid(row=2,column=2)

b8=Button(w, text=8, width=5, height=1, font=('Lucida Fax',20), bg='gray', command=lambda:number(8))
b8.grid(row=2,column=3)

b9=Button(w, text=9, width=5, height=1, font=('Lucida Fax',20), bg='gray', command=lambda:number(9))
b9.grid(row=3,column=0)

b0=Button(w, text=0, width=5, height=1, font=('Lucida Fax',20), bg='gray', command=lambda:number(0))
b0.grid(row=3,column=1)


b_add=Button(w, text="+", width=5, height=1,font=('Lucida Fax',20), bg='gray',fg='blue', command=lambda:operation('+'))
b_add.grid(row=3,column=2)

b_sub=Button(w, text="-", width=5, height=1,font=('Lucida Fax',20), bg='gray',fg='blue', command=lambda:operation('-'))
b_sub.grid(row=4,column=0)

b_eql=Button(w, text="=", width=5, height=1, font=('Lucida Fax',20), bg='gray',fg='blue', command = eql)
b_eql.grid(row=3,column=3)

b_mult=Button(w, text="×", width=5, height=1, font=('Lucida Fax',20), bg='gray',fg='blue', command = lambda:operation('×'))
b_mult.grid(row=4,column=2)

b_div=Button(w, text="÷", width=5, height=1, font=('Lucida Fax',20), bg='gray', fg='blue',command = lambda:operation('÷'))
b_div.grid(row=4,column=1)

b_clear=Button(w, text="CLEAR", width=5, height=1, font=('Lucida Fax',20), bg='gray', fg='brown',command = clear)
b_clear.grid(row=4,column=3)

w.mainloop()