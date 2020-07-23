# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 07:14:05 2020

@author: marti
"""

#%%

#about grid system

from tkinter import *
root = Tk()  #First thing to do

e= Entry(root, width=50,bg='blue',fg='white')

e.pack()

e.insert(0, 'Enter you name') #will put a default text in the text box. 0 is an index I dont understand

t=e.get()    #keeps what you wrote for whatever you need 

def myclick():    #what will happen when you click the button
    myLabel1= Label(root, text=t)
    myLabel1.pack()  
    


myButton=Button(root, text="Your name!", command=myclick, padx=50, pady=30)   #Define the thing
myButton.pack()                           # put it in the screen







root.mainloop()