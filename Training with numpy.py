#!/usr/bin/env python
# coding: utf-8

# In[2]:



import numpy as np

np.set_printoptions(precision=3) #Will write floats with just 3 decimals


# In[9]:


#Creating arrays
a=np.arange(1,20,2)
a2=a**2
print (a)

zeros=np.zeros((14,10)) #creates 2x10 dimension array   (14,10 is a tuple!!!)
print (zeros.shape, len(zeros))

ones=np.ones((100,2,5))
print ('ones  ', ones.ndim, ones.shape) #ndim=number of dimensions

manypoints=np.linspace(0,10,50)  #From 0 to 10, 50points
print (' Manypoints : ',manypoints.ndim, manypoints.shape)
xs = np.logspace(0,1, 20)  #linspace vs logspace
print (' Many points log scale: ',xs)

c=(3,8)  # c is a tuple
c_array=np.zeros(c) #and a tuple is the argument for .zeros or .ones or. eye
print (c_array)


# In[44]:


#creating arrays and reshaping
for_reshape=np.arange(0,24,2)
reshape=for_reshape.reshape(2,6)
print (for_reshape)
print (reshape)


# In[45]:


#Creating array from np.fromfunction(f,(x,y))

f=lambda a,b: a**2+2*b+3
my_array=np.fromfunction(f,(4,3))  #creates an 4x3 array. Indexes comes in the function
print (my_array)


# In[46]:


#Info about an array
print(my_array.shape)
print(my_array.ndim)
print(my_array.size)
print(my_array.dtype)
print(my_array.data)


# In[47]:


#Combining arrays
arr_a=np.arange(0,10,2) #start,end,step
print (arr_a)
arr_b=np.arange(1,11,2)
print (arr_b)
arr_sum=arr_a+arr_b
print ('sum...',arr_sum)

arr_zero=np.zeros((2,5))                  #one way to stack arrays...
arr_zero[0,:], arr_zero[1,:]=arr_a, arr_b
print (arr_zero)


# In[48]:


#another way to concatenate/stack  arrays...

arr_concat=np.concatenate((arr_a,arr_b))
print ('simple concatenation, if no axis is referred, flat concat is done...',arr_concat)

arr_stack_axis1=np.stack((arr_a,arr_b),axis=1)
arr_stack_axis2=np.stack((arr_a,arr_b),axis=0)          #other methods vstack and hstack can do same job

print ('Stack along axis 1...\n',arr_stack_axis1,' \n','Stack along axis 2...\n', arr_stack_axis2)


# In[49]:


#Transpose...
print (arr_stack_axis1, 'with .T \n',arr_stack_axis1.T)      #with .T
print ('with np.transpose(array)\n',np.transpose(arr_stack_axis1))


# In[50]:


#Basic operations
arr_zero[0,0]=0.1
print ('shape....', np.shape(arr_zero))
arr_log=np.log(arr_zero)
print (arr_log)
print (arr_zero*2)
print ('Sum of all values...',np.sum(arr_zero*2))
print (arr_zero * arr_zero)
arr_suma_ax1=np.sum(arr_zero,axis=0)
print ('Exemple with axis=0...', arr_suma_ax1)
print ('Mean axis 1...', np.mean(arr_zero, axis=1))


# In[51]:


#Boolean...
print (a==a2) #compares two arrays I created before, where a2 is a squared


# In[52]:


#np.random                    More random at the bottom
print (np.random)
print (np.random.rand(4),'...between 0. and 1.')
print ('\n4x4 dim array...between 0. and 1.\n',np.random.rand(4,4),)
print (np.random.randint(4))
chance=np.random.randn(1000)  #Gaussian random distribution (....normal?, se visualization)
binom=np.random.binomial(30,0.3,900)



# In[53]:


#More basic operations in array 'chance'
print ('min and max values',chance.min(),chance.max())
print ('\nIndex of those values\n',chance.argmin(),chance.argmax()) #index for the min and max values
rnd=np.random.rand(2,3)
print ('random multiD array:\n',
       rnd)
print ('by axis:', rnd.min(axis=0),rnd.max(axis=1))  #first array min value in every column, #second array max value in rows.

print (rnd.sort(axis=0))


# In[54]:


from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
#allow visualization IN the notebook
plt.plot(3*a2)
plt.show

plt.figure()
plt.hist(chance)
plt.show


# In[70]:


#Most exemples start with assigning a "random generator" to a conventional variable.
#e.g. for binomial distribution
rng = np.random.default_rng()          #Where default_rng is the default random generator.
n, p = 10, .5  # number of trials, probability of each trial
s = rng.binomial(n, p, 1000)           #but I could write as well random.binomial...
t = np.random.binomial(n, p, 1000)
plt.hist(s,histtype='step',color='r')
plt.hist(t,histtype='step',color='blue')
plt.show()

mu=0
sigma=30
bins=100
normal=rng.normal(mu,sigma,10000)  #binomial distribution,random...mean,std,n
plt.hist(normal,bins=bins)
#plt.show()

mu_calculated=np.mean(normal)        #to plot the lineal function
sigma_calculated=np.std(normal)
plt.plot(bins, 1/(sigma_calculated * np.sqrt(2 * np.pi)) 
         *np.exp( -(bins - mu_calculated)**2 / (2 * sigma_calculated**2) ),ls=':', lw=5)
print (sigma_calculated,mu_calculated)
plt.show()


# In [x]: mu, sigma = 100., 8.
# In [x]: samples = np.random.normal(loc=mu, scale=sigma, size=10000)
# In [x]: counts, bins, patches = pylab.hist(samples, bins=100, normed=True)
# In [x]: pylab.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
# ... np.exp( -(bins - mu)**2 / (2 * sigma**2) ), lw=2)
# In [x]: pylab.show()

# In[150]:


#Coool image...
image = np.random.rand(30, 30)    #Creates a radom matrix 30,30 with values between 0.0-1.0
print (np.median(image))
plt.imshow(image, cmap=plt.cm.hot)    

plt.colorbar()    
plt.show()


# In[53]:


#The usual python idiom for reversing a sequence is supported:
d=np.arange(5)
print (d)
print(d[::-1])


# In[216]:


#nan and infinite.
g=np.arange((10))
g=g/0
print (g)    #nan when mathematical operation difficult or not logical. inf when /0
print (np.isnan(g),np.isinf(g))


# In[16]:


#load from a file...that I created from eurostat...quite a mess with the format...
beds=np.genfromtxt(r'C:\Users\marti\Dropbox\Openstax Coursera Python\Python\my_programs\Training with\hospital_beds.csv'                   ,delimiter=';',names=True,dtype=None,encoding='L1')  #names for headers, dtype:if don´t write you get nan.
print (beds)  #should return an array with EU countries and number of beds / 100000habs.
#print (np.shape(beds))  #should be a two dimension 18,18 but is a one dimension 36. You could have written np.ndim(beds)

#x=beds[1][0]   #Look at this!!! you get the first object of the second tuple!!
#type(x)   to know the type of the variable

#split beds array in two.
beds_country=np.zeros(36,dtype=[('country','|S50'),('beds','f8')] )
#print (beds_country)  

                      
for i in range(0,36):                           #at the bottom you find a wiser way to exclude "wrong" data based on try except
    beds_country[i][0]=beds[i][0]               #index can be integers, slices, columnnames, BOOLEANS
    if beds[i][0]=='Albania':
        beds[i][1]=np.nan
    else:
        beds_country[i][1]=float(beds[i][1])
print ('As in pandas, just the country...',beds_country['country'])
print ('Mean number of beds per 10e5 inhab: ',np.mean(beds_country['beds']))




# In[321]:


#sorting (structured) arrays... with sort

beds_country.sort(order='beds')
print (beds_country)

#And if you want to sort when two countries have the same name -irrelevant in this case- you use...
beds_country.sort(order=['country','beds'])
#print (beds_country)


# In[39]:


#Another way to load. Notice that delimiter is ';'


def parse_beds(s):              #this function helps to convert to float a string which can't be converted (: in Albania)
    try:
        return float(s)
    except ValueError:
        return -99.            # returns a negative number that can be easily excluded later

dt=([('country','|S70'),('beds','f8')])   #this list of tupples define column name and data type. 


beds_2=np.loadtxt('hospital_beds_train_numpy_loadtxt.csv',dtype=dt,delimiter=';',                  skiprows=2,                     #skip rows= how many rows will be skipped in the original file
                  usecols=(0,1),                  #which columns will be used. I just have 2. But if 4, I may choose 0,2 and 3, eg.
                  converters={1: parse_beds})     #helps in case wrong data, as in (Albania,   : instead of a number)

valid_beds=beds_2['beds']>0      #boolean, notice [-3] is false (not >0) and corresponds to Albania, that now has -99 beds.
print (valid_beds)

mean_beds=beds_2['beds'][valid_beds]  #by doing this Albania not included.
print ('Mean beds per 10e5 inhab in EU : {:} '.format(np.mean(mean_beds)))

