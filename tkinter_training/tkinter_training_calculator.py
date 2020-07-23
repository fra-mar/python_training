# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 07:14:05 2020

@author: marti
"""

#%%

#about grid system

from tkinter import *
root = Tk()  #First thing to do
root.title('Simple calculator')
root.geometry("290x320+300+300") #The two last parameter where in the screen the window shows up

e= Entry(root, width=35, borderwidth=5,bg='blue',fg='white')

e.grid(row=0,column=0,columnspan=3, padx=10,pady=20)

#e.insert(0, 'Enter you name') #will put a default text in the text box. 0 is an index I dont understand

  #keeps what you wrote for whatever you need 

expr=""
def button(i):    #what will happen when you click the button
    global expr        #GLOBAL!!!! makes a local -in function- defined variable go global!!
  
    e.delete(0,END)
    expr = expr+i
    e.insert(0, expr)
    #temp_int=int(temp)
    return 


def button_equalix(): 
    e.delete(0,END)
    global expr
    result=eval(expr)     
    e.insert(0,result)
    expr=str(result)
    return 

def button_clear():
    e.delete(0,END)
    global expr
    expr=""

    
#define buttons
button_1=Button(root, text="1",command = lambda: button('1'),padx=40,pady=20)  #dan´t call a function with (), therefore you use lambda
button_2=Button(root, text="2",command = lambda: button('2'),padx=40,pady=20)
button_3=Button(root, text="3",command = lambda: button('3'),padx=40,pady=20)

button_add=Button(root, text="+",command =  lambda: button('+'),padx=39,pady=20)
button_minus=Button(root, text="-",command = lambda:  button('-'), padx=41,pady=20)
button_equal=Button(root, text="=",command = button_equalix,padx=88,pady=50)
button_clear=Button(root, text="clear",command = button_clear,padx=129,pady=20)

#put buttons on screen
button_1.grid(row=1,column=0)
button_2.grid(row=1,column=1)
button_3.grid(row=1,column=2)

button_add.grid(row=2,column=0)
button_minus.grid(row=3,column=0)
button_equal.grid(row=2,column=1,columnspan=2,rowspan=2)
button_clear.grid(row=4,column=0,columnspan=3)










root.mainloop()