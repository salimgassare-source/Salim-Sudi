import sqlite3
from tkinter import*
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox

class BackEnd():
    def __init__(self):
        pass

    def create_table(self):
        conn = sqlite3.connect('watu.db')
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS members(
                id INTEGER PRIMARY KEY,
                fn TEXT,
                sn TEXT,
                amt INTEGER)
            ''')
    
        conn.commit()
        conn.close()

    
    def fetch_customers(self):
        conn = sqlite3.connect('watu.db')
        cursor = conn.cursor()
        cursor.execute("SELECT* FROM members")
        e = cursor.fetchall()
        
        conn.close()
        return e

    
    def id_exists(self,id):
        conn = sqlite3.connect('watu.db')
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM members WHERE id=?',(id,))
        result=cursor.fetchone()
        conn.close()
        return result[0]>0


    def insert_customer(self,id, fn, sn, amt):
        conn = sqlite3.connect('watu.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO members (id,fn, sn,amt) VALUES(?,?,?,?)',(id, fn, sn,amt))
        conn.commit()
        conn.close()
    

    def earn_points(self,a,r):
        conn = sqlite3.connect('watu.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE members SET amt =amt+? WHERE id =?",(a,r))
        cursor.execute('SELECT* FROM members') 
        global e
        global p
        e = cursor.fetchall()[r-1]
        p=int(e[3])
    
        conn.commit() 
        conn.close()
        
        
    def redeem_points(self,a,r):
        conn = sqlite3.connect('watu.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE members SET amt =amt-? WHERE id =?",(a,r))
        cursor.execute('SELECT* FROM members') 
        global e
        global p
        
        e = cursor.fetchall()[r-1]

        p=int(e[3])
       
        conn.commit() 
        conn.close()
        return p
        
    def edit_customer(self,fn,sn,r):
        conn = sqlite3.connect('watu.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE members SET fn =?, sn=? WHERE id =?",(fn,sn,r))
        cursor.execute('SELECT* FROM members') 
        
        conn.commit() 
        conn.close() 



w =Tk()
w.geometry('1000x600')
w.title('SMART-SELL POS,   @TOP.TECHNOLOGIES, powered by creativity        VERSION 1.0')
#picture=PhotoImage(file="smartLogo.png")
#image_logo =Label(w,image =picture, compound="bottom")
#image_logo.pack()

class FrontEnd(BackEnd):

    def __init__(self):
        pass

    def registration(self):
        w=Tk()
        w.geometry('800x600')
        w.title('SMART-SELL POS,   @TOP.TECHNOLOGIES, powered by creativity        VERSION 1.0')

        l0 =Label(w, text= "Enter Member Number")
        l0.grid(row=0,column=0)
        e0 =Entry(w)
        e0.grid(row=0,column=1)
        l1 = Label(w, text ='Enter First Name')
        l1.grid(row=1,column=0)
        e1 =Entry(w)
        e1.grid(row=1,column=1)

        l2 = Label(w, text ='Enter Second Name')
        l2.grid(row=2,column=0)
        e2 =Entry(w)
        e2.grid(row=2,column=1)

        l3 = Label(w, text ='Points')
        l3.grid(row=3,column=0)
        e3 =Entry(w)
        e3.grid(row=3,column=1)


        style = ttk.Style(w)
        style.theme_use('clam')
        style.configure('Treeview', fg='#fff', bg='#000', fieldbackground='#313837')
        style.map('Treeview', background=[('selected', '#1A8F2D')])

        tree = ttk.Treeview(w,height=27)

        tree['column']=('A', 'B', 'C','D')

        tree.column('#0', width=0,stretch=tk.NO)
        tree.column('A', anchor=tk.CENTER, width=120)
        tree.column('B', anchor=tk.CENTER, width=120)
        tree.column('C', anchor=tk.CENTER, width=120)
        tree.column('D', anchor=tk.CENTER, width=120)
    
        tree.heading('A', text ='CODE')
        tree.heading('B', text ='FIRST NAME')
        tree.heading('C', text ='SECOND NAME')
        tree.heading('D', text ='POINTS')
        tree.place(x=300, y=20)
    
        def add_to_treeview():
            x= be.fetch_customers()
            tree.delete(*tree.get_children())
            for items in x:
                tree.insert('', END, values = items)


        def addMember():
            id=e0.get()
            e0.delete(0,END)

            fn=e1.get()
            e1.delete(0,END)

            sn=e2.get()
            e2.delete(0,END)

            amt=e3.get()
            e3.delete(0,END)

            if not(id and fn and sn and amt):
                #messagebox.showerror('Enter all Fields!')
                allFields=Label(w, text = 'Enter all fields !',fg='red')
                allFields.grid(row =5, column = 1)
                

            elif be.id_exists(id):
                #messagebox.showerror('ID already Exists!')
                idField=Label(w, text = 'code already exists !',fg='red')
                idField.grid(row =5, column = 1)
                
            else:
                be.insert_customer(id,fn,sn,amt)
                add_to_treeview()
                #messagebox.showinfo("customer successfully added")
                successful=Label(w, text = 'customer successfully added !',fg='green')
                successful.grid(row =5, column = 1)
                

        b1 = Button(w,text='Submit',fg ='blue',command=addMember)
        b1.grid(row=4,column=1)
        add_to_treeview()  
   

    def add_points(self):
        w=Tk()
        w.geometry('800x600')
        w.title('SMART-SELL POS,   @TOP.TECHNOLOGIES, powered by creativity        VERSION 1.0')

        l4 = Label(w, text ='Enter Amount')
        l4.grid(row=0,column=0)
        e4 =Entry(w)
        e4.grid(row=0,column=1)

        l5 = Label(w, text ='Enter Code')
        l5.grid(row=1,column=0)
        e5 =Entry(w)
        e5.grid(row=1,column=1)


        def points():
            a=int(e4.get())
            pt=a//30
            e4.delete(0,END)
            
            r=int(e5.get())
            e5.delete(0,END)

            be.earn_points(pt,r)

            leb =Label(w, text = e)
            leb.grid(row=6, column=4)
            lebo = Label(w, text='customer details: ')
            lebo.grid(row=6,column=3)

            lebz = Label(w, text='Points Earned: ')
            lebz.grid(row=7,column=3)
            lebz1 =Label(w, text=pt)
            lebz1.grid(row=7,column=4)

            lebo2=Label(w,text= 'total point balance: ')
            lebo2.grid(row=8,column=3)
            leb2=Label(w,text = p)
            leb2.grid(row=8, column=4)
  
        b2 = Button(w,text='save points',fg='blue',command=points)
        b2.grid(row=3,column=1)


    def redeeming(self):
        w=Tk()
        w.geometry('800x600')
        w.title('SMART-SELL POS,   @TOP.TECHNOLOGIES, powered by creativity       VERSION 1.0')

        l4 = Label(w, text ='Enter Points')
        l4.grid(row=0,column=0)
        e4 =Entry(w)
        e4.grid(row=0,column=1)

        l5 = Label(w, text ='Enter Code')
        l5.grid(row=1,column=0)
        e5 =Entry(w)
        e5.grid(row=1,column=1)

        def redeem():
            pt=int(e4.get())
            e4.delete(0,END)
            c=0
            r=int(e5.get())
            e5.delete(0,END)
            fe.redeem_points(c,r)

            if (p-pt)<0:
                leb =Label(w, text = e)
                leb.grid(row=6, column=4)

                lebo = Label(w, text='customer details: ')
                lebo.grid(row=6,column=3)

                lebz = Label(w, text='Points Redeemed: ')
                lebz.grid(row=7,column=3)
                lebz1 =Label(w, text=c)
                lebz1.grid(row=7,column=4)

                lebo2=Label(w,text= 'total point balance: ')
                lebo2.grid(row=8,column=3)
        
                leb2=Label(w,text = p)
                leb2.grid(row=8, column=4)

                errorLabel =Label(w,text = " Insufficient points !", fg = 'red')
                errorLabel.grid(row=9, column=4)
                
            else:
                be.redeem_points(pt,r)

                leb =Label(w, text = e)
                leb.grid(row=6, column=4)

                lebo = Label(w, text='customer details: ')
                lebo.grid(row=6,column=3)

                lebz = Label(w, text='Points Redeemed: ')
                lebz.grid(row=7,column=3)
                lebz1 =Label(w, text=pt)
                lebz1.grid(row=7,column=4)

                lebo2=Label(w,text= 'total point balance: ')
                lebo2.grid(row=8,column=3)
        
                leb2=Label(w,text = p)
                leb2.grid(row=8, column=4)
            

        b2 = Button(w,text='redeem points',fg='blue',command=redeem)
        b2.grid(row=3,column=1)


    def editing(self):
        w=Tk()
        w.geometry('800x600')
        w.title('SMART-SELL POS,   @TOP.TECHNOLOGIES, powered by creativity         VERSION 1.0')

        l0 =Label(w, text= "Enter Member Number")
        l0.grid(row=0,column=0)
        e0 =Entry(w)
        e0.grid(row=0,column=1)
        l1 = Label(w, text ='Enter First Name')
        l1.grid(row=1,column=0)
        e1 =Entry(w)
        e1.grid(row=1,column=1)

        l2 = Label(w, text ='Enter Second Name')
        l2.grid(row=2,column=0)
        e2 =Entry(w)
        e2.grid(row=2,column=1)
        
        def edit():
            r=e0.get()
            e0.delete(0,END)

            fn=e1.get()
            e1.delete(0,END)

            sn=e2.get()
            e2.delete(0,END)

            be.edit_customer(fn,sn,r)
            
        b2 = Button(w,text='edit customer',fg='blue',command=edit)
        b2.grid(row=3,column=1)


be=BackEnd()
fe =FrontEnd()


menubar = Menu(w)
w.config(menu=menubar)

pointsMenu = Menu(menubar)
menubar.add_cascade(label = 'EARN POINTS', command=fe.add_points)

redeemMenu = Menu(menubar)
menubar.add_cascade(label = 'REDEEM POINTS', command=fe.redeeming)

addMembers = Menu(menubar)
menubar.add_cascade(label = 'REGISTER MEMBERS',command = fe.registration)

editMenu = Menu(menubar)
menubar.add_cascade(label = 'EDIT MEMBERS',command = fe.editing)



w.mainloop()


