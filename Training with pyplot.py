#!/usr/bin/env python
# coding: utf-8

# In[14]:


#Training with matplotlib.pyplot
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[22]:


# read a dataframe from a previous exercise (GDP vs hospital beds vs doctors / 100 000 inhab)
df_gdp=pd.read_csv(r'C:\Users\marti\Dropbox\Openstax Coursera Python\Python\my_programs\Data_Eurostat\df_gdp_beds_grad.csv',header=0)
df_gdp.drop(columns='Unnamed: 0',inplace=True)
df_gdp.drop(index=[0,1,2],axis=0,inplace=True)
df_gdp.reset_index(inplace=True,drop=True)
#print (df_gdp.info())
print (df_gdp.head())

df_sorted=df_gdp.sort_values('GDP_capita',ascending=False)     #Descending sorted after gdp


# In[21]:


#read a file with EU GDP through years

df_gdp_evol=pd.read_excel(r'C:\Users\marti\Dropbox\Openstax Coursera Python\Python\my_programs\Data_Eurostat\Eurostat_GDP.xls',
                         header=2,skipfooter=8, usecols=(0,1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39),na_values=":")

df_gdp_evol.dropna(inplace=True,axis=0)#               Cleaning the data
df_gdp_evol.drop([0,1,2],inplace=True), df_gdp_evol.reset_index(inplace=True)
df_gdp_evol.set_index('geo/time',inplace=True)    #OBS!!! sets the index to the country name

# makes another dataframe with growth rate 2000-2019
df_evol=pd.DataFrame(index=df_gdp_evol.index)
df_evol['rate']=df_gdp_evol['2019']/df_gdp_evol['2000']
#print (df_evol.sort_values(by='rate'))
#print (df_evol)

#just for fun, GDP/capita by country, sorted
df_sorted_evol=df_gdp_evol.sort_values('2019',ascending=False) 
print ('GDP/capita by country, descending\n:', list(df_sorted_evol.index))


# In[23]:


#Basic plot

my_fig=plt.figure('gdp_capita_2019_EU',figsize=(8,4),facecolor=('0.9'),edgecolor='black')
my_ax=my_fig.add_subplot(1,1,1)

df_x=df_gdp_evol.loc['Spain'].reset_index()  #Select GDP/capita Spain 2000-2019
df_x.drop([0],inplace=True)                 

#print (df_x), print (df_x.info(verbose=True))
my_ax.plot(    range(0,len(df_x))  , df_x['Spain'],  linestyle='-.', color='#33089a', marker='D', markerfacecolor='#96f481') 

my_ax.set_ylim(20000,26000)


my_ax.set_xticks(range(0,len(df_x)) )
my_ax.set_xticklabels(df_x['index'],rotation=45)

my_ax.yaxis.grid(ls=':',c=('0.9'),lw=2, alpha=0.2)

my_ax.set_xlabel('Year')
my_ax.set_ylabel('GDP per capita')
my_ax.set_title('Spain')

my_ax.set_facecolor((1.0, 0.47, 0.42))   #change the color of the plot itself, not the surroundings. tuple RGB


plt.show()


#                                     ABOUT MARKERS
# Code Marker Description
# .  point
# o  circle
# +  plus
# x  x
# D diamond
# v  (downward triangle)
# ^  (upward triangle)
# s  square
# *  star
# 
# 
# 
# markersize ms Marker size, in points
# markevery Set to a positive integer, N, to print a marker every N
# points; the default, None, prints a marker for every point
# markerfacecolor mfc Fill color of the marker
# markeredgecolor mec Edge color of the marker
# markeredgewidth mew Edge width of the marker, in points

# In[24]:


#for every country

f=plt.figure(figsize=(8,8),facecolor=('0.9'),edgecolor='black')
ax=f.add_subplot(1,1,1)


countries=df_gdp_evol.index.tolist()
print (countries)
select=input ('Select a country: ')
nyears=len(df_gdp_evol.columns)-1
years=df_gdp_evol.columns[1:]

for i in range(0,len(df_gdp_evol)):
    df_x=df_gdp_evol.loc[countries[i]].reset_index()  #Select GDP/capita country(x) 2000-2019
    df_x.drop([0],inplace=True)     #first row just index and indexnumber for country(x)
  
    col=df_x.columns.tolist()
    if countries[i]==select:
        color='b'
        linestyle='-'
    else:
        color='#96f481'
        linestyle=':'
    ax.plot(    range(0,len(df_x))  , df_x[col[1]],  linestyle=linestyle, color=color) 
    


ax.set_xticks(range(0,nyears) )
ax.set_xticklabels(years,rotation=45)

ax.yaxis.grid(ls=':',c=('0.9'),lw=2, alpha=0.2)

ax.set_ylabel('GDP per capita')

ax.set_facecolor((1.0, 0.47, 0.42))   #change the color of the plot itself, not the surroundings. tuple RGB
title='EU GDP/capita. '+select+' highlighted'
ax.set_title(title)

plt.show()


# In[36]:


#Bars diagram    using df_sorted (gdp/capita, beds/10e5 hab, grad/10e5 hab -doctors-)

#First gdp/capita
f2=plt.figure(figsize=(16,6))
ax_gdp=f2.add_subplot(1,2,1)
ax_beds=f2.add_subplot(1,2,2)    

range_x=range(0,len(df_sorted))

ax_gdp.bar(range_x, df_sorted['GDP_capita'],color=(1.0, 0.47, 0.42))
ax_beds.bar(range_x, df_sorted.beds)

ax_gdp.set_xticks(range_x)
ax_gdp.set_xticklabels(df_sorted['GEO/TIME'],rotation=90)
ax_gdp.set_ylabel('GDP (euro)/capita. 2019')
ax_beds.set_xticks(range_x)
ax_beds.set_xticklabels(df_sorted['GEO/TIME'],rotation=90)
ax_beds.set_ylabel('Beds/100 000 inhab. 2017')

f2.subplots_adjust(left=0.1,right=0.9,wspace=0.15)  #fractional values of the figure’s height and width
#f2.subplots_adjust(left=0.0,right=0.3,wspace=0.2)  #eg. l+r+wspace=1 takes the whole length.
                                                    #...l=0.0,r=0.3,wspace=0.2 only 50% of length occupied by figure...
                                                    #....30% blank space to the right

f2.suptitle('GDP/capita and hospital beds /100 000 inhab in the EU.', fontsize=16  )     
plt.show()       #plt.tight_layout() makes things easier

##figure can be saved savefig(fname, dpi=None, facecolor='w', edgecolor='w',
        #orientation='portrait', papertype=None, format=None,
        #transparent=False, bbox_inches=None, pad_inches=0.1, frameon=None, metadata=None)        .....png default


# #Adjusting subplots
# To further customize the subplot spacing, call fig.subplots_adjust(). This
# method takes any of the keywords left, bottom, right, top, wspace and hspace,
# which can be set to fractional values of the figure’s height and width as appropriate
# to determine the positions of the subplots’ left side (default 0.125), right side (0.9),
# bottom (0.1), top (0.9), vertical spacing (0.2) and horizontal spacing (0.2). A practical
# use of this function is to create “ganged” subplots that share a common axis, as in the
# following example (the example takes hspace to 0)

# In[31]:


#Side by side bars



f3=plt.figure(figsize=(16,6))
ax_side=f3.add_subplot(1,1,1)
#gdp  x positions
n = 1  # This is our first dataset (out of 2)
t = 2 # Number of datasets
d = len(df_gdp) # Number of sets of bars
w = 0.8  # Width of each bar
x_gdp = [t*element + w*n for element
             in range(d)]
#beds s positions
n = 2  # This is our second dataset (out of 2)
#t = 2 # Number of datasets
#d = 7 # Number of sets of bars
#w = 0.8 # Width of each bar
x_beds = [t*element + w*n for element
             in range(d)]

ax_side_twin=ax_side.twinx()

ax_side.bar(x_gdp,df_sorted.GDP_capita,color=(1.0, 0.47, 0.42))
ax_side_twin.bar(x_beds,df_sorted.beds,label='Hosp beds/100000 hab')

ax_side.set_xticks(range(1,2*d,2))
ax_side.set_xticklabels(df_sorted['GEO/TIME'],rotation=90)
ax_side.set_ylabel('GDP (euro)/capita. 2019')
ax_side_twin.set_ylabel('Hospital beds / 100 000 inhab, scale corrected to match GDP')

#ax_beds.set_xticklabels(df_gdp['GEO/TIME'],rotation=90)

#setting a secondary axis for beds

#secax = ax.secondary_xaxis('top', functions=(deg2rad, rad2deg))
#secax.set_xlabel('angle [rad]')

# Another way, without calling functions
#fig, ax1 = plt.subplots()
#ax2 = ax1.twinx()
#ax1.plot(x, y1, 'g-')
#ax2.plot(x, y2, 'b-')



plt.show()



# #Side by side bars how to calculate distances
# 
# #China data blue bars
# n = 1  # This is our first dataset (out of 2)
# t = 2 # Number of datasets
# d = 7 # Number of sets of bars
# w = 0.8 # Width of each bar
# x_values1 = [t*element + w*n for element
#              in range(d)]
# 
# #US data oranga bars
# n = 2  # This is our second dataset (out of 2)
# t = 2 # Number of datasets
# d = 7 # Number of sets of bars
# w = 0.8 # Width of each bar
# x_values2 = [t*element + w*n for element
#              in range(d)]
# 
# 

# In[28]:


#from exemple in stackoverflow:   look how figure and axes are defined...and tight_layout()
import numpy as np
#from scipy.stats import kurtosis, skew 

x_random = np.random.normal(0, 2, 10000)

x = np.linspace( -5, 5, 10000 )
y = 1./(np.sqrt(2.*np.pi)) * np.exp( -.5*(x)**2  )  # normal distribution



f, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(12, 5))                    #OBS!!!!    subplotSSSSS, not subplot
ax1.hist(x_random, bins='auto')
ax1.set_title('probability density (random)')
ax2.hist(y, bins='auto')                                #intersting bins='auto'
ax2.set_title('(your dataset)')
plt.tight_layout()               #look at documentation for aditional parameters https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.tight_layout.html


# In[ ]:




