# -*- coding: utf-8 -*-
#Training reading and writing files

from datetime import *
from time import sleep


"""
Creates a file in "writing" mode. So everytime you run script
old date erased. To add data open it in append mode "a"
"""
with open ("writing_files.csv", "w") as f:
    
    for i in range (0,5):
        
        now =datetime.now()
    
        h, m ,s= now.hour, now.minute, now.second
    
    
        to_write=str(h)+ ',' + str(m)+',' + str(s) +"\n"
    
        f.write(to_write)
        
        sleep(2)
    
#%% opening
with open ("writing_files.csv", "r") as ff:
    
    to_show= ff.read()   #gets the whole file as it is, text
    
    print (to_show)
    
#%% opening one line at a time    
with open ("writing_files.csv", "r") as ff:
    
    
    first_line = ff.readline()    #read one line
    second_line = ff.readline()    #read one line
    
    
    print ("first line", first_line)
    print ("second line", second_line)
    
#%% opening all lines    
with open ("writing_files.csv", "r") as ff:
    
    all_lines= ff.readlines()   #get all lines  =  list of lines
    
    print ("all lines:\n", all_lines)
    