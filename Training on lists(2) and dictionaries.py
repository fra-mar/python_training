#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Training with lists 2. 
#Lists of lists


# In[1]:


#Coordinates
place_a=[3,7]; place_b=[2,10]; place_c=[1,9]
all_places_list=place_a+place_b+place_c
print (all_places_list, 'as list1+list2+list3')

my_places=[]
my_places.append(place_a)
print (my_places,'    as .append')
my_places.extend((place_b,place_c))
print (my_places,'    as .extend')

#Just to get a longer list, I multiply my_places x 5
many_places=my_places*3
print ('\nMany places:  ',many_places)

#Show every second index
print ('\nEvery second index:   ',many_places[::2])
print ('\nEvery third index starting in the second item:   ',many_places[1::3])




# In[3]:


#as a dictionary
dictionary={'a':my_places[0], 'b':my_places[1], 'c':my_places[2]}
print (dictionary)
print (dictionary.get('a'))
dictionary.update({'d':[12,0],'e':[34,5]})
print (dictionary)
#Dear Pitagoras

a=dictionary.get('a'); print (type(a))
b=dictionary.get('b')
c=dictionary.get('c')
calculate_distance=lambda p1,p2: ((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)**(1/2)

print ('Distance a_b: ',calculate_distance(a,b))
print ('Distance a_c: ',calculate_distance(a,c))

