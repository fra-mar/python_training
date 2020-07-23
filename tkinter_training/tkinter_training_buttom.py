# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 07:14:05 2020

@author: marti
"""

#%%

#about grid system

from tkinter import *
root = Tk()  #First thing to do

def myclick():    #what will happen when you click the button
    myLabel1= Label(root, text="I clicked!")
    myLabel1.grid(row=0,column=1)    
    
def otherclick():
    myLabel2=Label(root, text = "You pushed!")
    myLabel2.grid(row=1,column=1)

myButton=Button(root, text="Click me!", command=myclick, padx=50, pady=30)   #Define the thing
myButton.grid(row=0,column=0)                            # put it in the screen

otherButton=Button(root, text="Push",fg='blue',bg='green',padx=50,pady=50,command=otherclick)
otherButton.grid(row=1,column=0)






root.mainloop()