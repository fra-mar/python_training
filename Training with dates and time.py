#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from datetime import datetime
from datetime import timedelta


# In[2]:


#How old are you...from your pn or birthdate
pn=input ('Skriv pn i format ÅÅÅÅMMDD-XXXX: ')
pn_list=list(pn)
del pn_list[-5:]

yr,mo,da="","",""
for i in range(0,4):
    yr=yr+pn_list[i]
for i in range (4,6):
    mo=mo+pn_list[i]
for i in range (6,8):
    da=da+pn_list[i]

birthday=yr+' '+mo+ ' '+ da

birthday_delta=datetime.now()-datetime.strptime(birthday,'%Y %m %d')
print ('Look at different ways to express timedelta\n')
print (birthday_delta)
print (birthday_delta.days)
print (birthday_delta.days/365, ' years')

def splitdays(days_to_split):
    years=days_to_split.days//365
    months=((days_to_split.days/365-days_to_split.days//365)*365)//30.5
    days=(days_to_split.days%365)%12
    result=str(years)+ ' years, '+str(months)+' months, '+str(days)+ ' days.'
    return result

print ('\nI used a function to split days in yr, mo, dd:')
print (splitdays(birthday_delta))


# In[63]:


#Training with timedelta (OBS must be imported from datetime)

delta=timedelta(seconds=2)
now=datetime.now()
while now+delta>datetime.now():
    a=0
print ('........now!')


# In[87]:


#calculate datetime after a timedelta.
timefuture=input('Write a date in format YYYY-MM-DD: ')
timefuture_parsed=datetime.strptime(timefuture,'%Y-%m-%d')
delta=timefuture_parsed-datetime.now()
print (delta)
print (delta.days)
print ('\nWith my function to split days in yr,mo,da...')
print (splitdays(delta))


# In[98]:


#printing just year, month...
now=datetime.now()
print ('Row...', now)
print(now.year)
print (now.month)
print (now.day)
print (now.hour)
print (now.minute, 'minutes')
print (now.weekday(), '...days of the week, where 0=monday, 1= tuesday...')


# In[121]:


#Calls at 2s intervals during 12 s
now=datetime.now()
t0=now
print ('Start!',t0)
while datetime.now()<(now+timedelta(seconds=12)):
    if datetime.now()>t0+timedelta(seconds=2):
        print ('Ping! ',t0.minute,' min, ',t0.second,'  secs ')
        t0=datetime.now()

print ('Stop')   

