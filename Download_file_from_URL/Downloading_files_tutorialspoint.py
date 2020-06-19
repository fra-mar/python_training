# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 05:52:08 2020

@author: marti
"""
#This first block download excel file folkhälsomyndigheten website with data about COVID19 cases in Sweden.

import requests

url='https://www.arcgis.com/sharing/rest/content/items/b5e7488e117749c19881cce45db13f7e/data'

r=requests.get(url, allow_redirects=True)

open('data_fhm.xls','wb').write(r.content)     #Save the content with name

#%% Explores...So let’s first get the type of data the url is linking to−
print(r.headers.get('content-type'))


#%% Look if it works..
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
df=pd.read_excel('data_fhm.xls', sheet_name='Antal avlidna per dag')

df['datum']=df.Datum_avliden    #Set the date in a nicer format to be plotted

for i in range(0,len(df.datum)-1):
      
    df.datum[i]=datetime.strftime(df.Datum_avliden[i],format='%Y-%m-%d')
    
plt.bar(df.datum,df.Antal_avlidna)
plt.show()
#%%
print (df.datum.tail())