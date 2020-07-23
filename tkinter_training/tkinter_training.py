# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 07:14:05 2020

@author: marti
"""

from tkinter import *
#in tkinter everything is a widget
root = Tk()  #First thing to do

#Create something is a two step process, define it and then put it in scren
myLabel = Label(root, text=" aaaaa aaaa")   #defined

myLabel.pack()   #easiest way toput something in screen



#Create always an event loop: looping all the time so machine senses what you do.
root.mainloop()
#%%

#about grid system

from tkinter import *
root = Tk()  #First thing to do

#Create something is a two step process, define it and then put it in scren
myLabel1 = Label(root, text=" aaaaa aaaa")   #defined
myLabel2 = Label(root, text=" bbbbb")

myLabel1.grid(row=0, column=0) 
myLabel2.grid(row=1, column=0) 



#Create always an event loop: looping all the time so machine senses what you do.
root.mainloop()