#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Trainig with numpy data fitting
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd


# In[13]:


#I create an array with a sine function and add some random to the data
rand_normal=np.random.normal(0,0.1,20)

x=np.linspace(0,np.pi,20)+rand_normal*3

y=np.sin(x)+rand_normal   #my function


# In[16]:


import numpy.polynomial.polynomial as poly

plt.scatter(x,y)   #plot my 'raw' data

x_new = np.linspace(x[0], x[-1], num=len(x)*10)    #get an 'ideal' x to test the 'y' against.

coefs = poly.polyfit(x, y, 2)
ffit = poly.polyval(x_new, coefs)   #polyval does the opposite: you give polynomial coefficients and it returns y values
                                    #i.e. ffit is a fitted function
plt.plot(x_new, ffit)

plt.show()


# In[7]:


#Another way to put it
ffit_just_coefficients = poly.Polynomial(coefs) 

print (ffit_just_coefficients)

plt.plot(x_new, ffit_just_coefficients(x_new))
print ('When x=2.7, y equals...',ffit_just_coefficients(2.7))
print (poly.polyval(2.7,coefs))
       

plt.show()


# In[8]:


#polyfit returns a list of coefficinets, highest power first

for i in range(0,len(coefs)):
    lista=[a for a in range(len(coefs)-1,-1,-1)]
    print ('Power ',lista[i],' coef ',coefs[i])


#polyval returns an (y) value from a list of coefficients
np.polyval([3,0,1], 5)  # 3 * 5**2 + 0 * 5**1 + 1   should yield 76

print ('np.polyval...wrong number but no idea why ',np.polyval(coefs,2.7))
print ('np.polynomial.polynnomial as poly ',poly.polyval(2.7, coefs))


# In[11]:


#applied to reality. COVID19 deaths in Sweden.
daily_deaths=pd.read_excel(r'C:\Users\marti\Dropbox\Openstax Coursera Python\Python\my_programs\CovidProjects\Folkhalsomyndigheten_Covid19.xlsx',
                            sheet_name='Antal avlidna per dag')
deaths=np.array(daily_deaths['Antal_avlidna'])
x=np.arange(len(deaths))

coefs = poly.polyfit(x, deaths, 4)         #This is the core of the procedure
ffit = poly.polyval(x, coefs)

print ('estimated death day 100 ',poly.polyval(100,coefs))


plt.plot(x,ffit)                           #Obviously this is not valid (science). Only plateau should be analized due to...
plt.scatter(x,deaths)                      #first is the start. Many measures were taken. Last days not reliable due to late report
plt.show()


x_sim=np.linspace(0,100,250)               #But be carefull with functions cause long term prognosis can be pretty unaccurate
ffit = poly.polyval(x_sim, coefs)          # if many 'degrees' (try 4)
plt.plot(x_sim,ffit)
plt.show()

