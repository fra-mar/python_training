#!/usr/bin/env python
# coding: utf-8

# In[84]:


#Check https://scipy-lectures.org/intro/language/basic_types.html#lists
#  my_list.    .append .count   .extend    .insert    .pop    
#              .remove    .reverse    .sort   .index


# In[85]:


#I create a (list) deck of cards
numbers=[x for x in range(1,11)]
numbers_faces=[str(x) for x in numbers]
                
numbers_faces.extend(['J','Q','K'])
#.append had given ...'9', '10', ['J', 'Q', 'K']]
kinds=['H','S','D','C']
deck=[]
for i in range (0,4):
    for b in range(0,13):
        card=str(numbers_faces[b]+kinds[i])
        deck.append(card)
        
print (deck)

backup=deck  #to be used down after I´ve trained with other commands


# In[86]:


print (deck.count('JC'))
print (deck.index('4S'))
deck.sort()
deck.insert(1,'heeelllllowww...ERASE ME')
print (deck[:10],  'interrupted at index 3', str(len(deck)))
deck.remove('heeelllllowww...ERASE ME')                    #difference between .remove and del  list([index])
print (deck[:10],  'interrupted at index 3', str(len(deck)))
deck.insert(1,'heeelllllowww...ERASE ME')
print (deck[:10],  'interrupted at index 3', str(len(deck)))
del deck[1]
print (deck[:10],  'interrupted at index 3', str(len(deck)))
type (deck)


# In[87]:


z=deck.pop(1)
print ('Popped item: ',z, '    Remaining:', deck[0:10], '...')

#insert the popped item
deck.insert(1,z)
print ('Popped item: ',z, ' ...is back    As it was...:', deck[0:10], '...')


# In[89]:


#shuffle the deck
import random
deck=backup
random.sample(deck,k=52)
print (deck)


# In[81]:


#shuffle and select 4 cards, whithout replacing them

deck=backup
while len(deck)>=4:
    to_discard=random.sample(deck,k=4)
    print (to_discard, '    ', str(len(deck)))
    for i in to_discard:
        deck.remove(i)
    


# In[ ]:




