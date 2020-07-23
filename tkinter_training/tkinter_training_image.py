# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 07:14:05 2020

@author: marti
"""

#%%

#how to create an ico file for logo, both with a website app and with paint in...
#...https://www.wikihow.com/Create-a-Windows-Icon#Creating-an-Icon-in-Paint

from tkinter import *
root = Tk()  #First thing to do
root.title('Tkinter images')
root.iconbitmap('tkinter_train_icon.ico')

quit_button=Button(root, text='Exit program', command= root.quit)

quit_button.pack()

#%%
#how to manage images
#Tkinter manages just .gif For other formats another module is needed. PIL is old but has modifications...
#Another useful library is Pillow. Not installed by default. In command line you write > pip install Pillow

from PIL import ImageTk,Image

#Adding images is not a 2 but a 3 step process. Define image > put it in something else > show in the screen

my_image= ImageTk.PhotoImage(Image.open('images/mars.jpg'))   #Define image
my_label = Label(image=my_image)                   #put it in somethign else
my_label.pack()

root.mainloop()