#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Training with structured arrays in np.           genfromtxt down
#Based on https://scipython.com/book/chapter-6-numpy/examples/using-numpys-loadtxt-method/
import numpy as np


# In[2]:


fname = 'eg6-a-student-data.txt'
dtype1=np.dtype([('gender','|S1'),('height','f8')])
a=np.loadtxt(fname, dtype=dtype1, skiprows=9, usecols=(1,3)) #skiprows sleaps the first 9 rows
print (a)
a.dtype


# In[3]:


#finding mean height of males
m= a['gender']==b'M'
print(m)  

height_m=a['height'][m]       #index can be integers, slices, columnnames, BOOLEANS
height_f=a['height'][~m]

median_m=str(np.median(height_m))
median_f=str(np.median(height_f))

#print('Male average: {:.2f} m, Female average: {:.2f} m'.format(median_m, median_f))
print ('Median height males: {:} m. Median height females: {:}m'.format(median_m, median_f))


# In[5]:


#now weight...and the problem is that som data is missing...
dtype2=([('gender','|S1'),('weight','f8')])


def parse_weight(s):
    try:
        return float(s)
    except ValueError:
        
        return -99
    

b=np.loadtxt(fname,dtype=dtype2,skiprows=9,usecols=(1,4),            converters={4:parse_weight})

#print (b)
bool_valid_b=b['weight']>0
valid_b=b[bool_valid_b]       #the new array valid_b doesn´t include wrong data (those that parse_weight defined as -99)
#print (valid_b)
are_m=valid_b['gender']== b'M'

median_weight_men=np.median(valid_b['weight'][are_m])
median_weight_women=np.median(valid_b['weight'][~are_m])

print ('Median weight men is {:} Kg. For women is {:} Kg. '.format(median_weight_men, median_weight_women))


# In[14]:


#Setting every column in a different array.....unpack in loadtxt or genfromtxt

dtype3=([('gender','|S1'),('bp','|S7')])
gender, bp = np.loadtxt(fname,dtype=dtype3,skiprows=9,usecols=(1,5),            unpack=True)                                                  #look!!!, you can assign 2 arrays to 2 columns from start!!
                                                                          #by setting unpack to true!
bp_split=np.zeros((len(bp),2))  # bpbp.split('/')
for i in range(0,len(bp)):
    a=str(bp[i]).split('/')
    a[0]=a[0].strip("'b''")                                               #This is a painful process to separate BP in S and D
    a[1]=a[1].strip("'")
    try:
        bp_split[i][0]=int(a[0])
        bp_split[i][1]=int(a[1])
    except ValueError:
        bp_split[i][0]=-5
        bp_split[i][1]=-5


print (bp_split)


# In[113]:


#here I train with genfromtxt and differences with loadtxt

fname='train_genfromtxt_missing.txt'
dtype4=([('participant','i4'),('gender','S1'),('Tblack','f8'),('Tcolor','f8')])
missing_not_filling=np.genfromtxt(fname,dtype=dtype4,usecols=(1,2,3),delimiter=',',                     skip_header=1,skip_footer=1,                    missing_values={2:'X',3:'-'},                    filling_values={2:-1,3:-1})      #here the method understands how a wrong data looks like in each column
                                                     # and with filling_values understands how to replace them
#print (missing_not_filling)                        #if filling_values is not defined then genfromtxt replace with...see below

stroop=np.genfromtxt(fname,dtype=dtype4,usecols=(1,2,3),delimiter=',',skip_header=1,skip_footer=1,                    missing_values={2:'X',3:'-'})

#print (stroop)                                      #in this case nan.

#selecting cases with all the data ok.

# Remove invalid rows from data set
filtered_data = stroop[ np.isfinite(stroop['Tblack']) & np.isfinite(stroop['Tcolor'])  ]

#above, nice exemple how to select data with booleans inside brackets.

print (len(stroop)-len(filtered_data), ' cases were removed')

mu_black, sigma_black= np.mean(filtered_data['Tblack']), np.std(filtered_data['Tblack'])   #exemple how can you assign two variables at once.

print ('Students read the black letters in {:.2f}({:.2f}) s  ( mean(std) )'.format(mu_black,sigma_black))

