# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 08:59:35 2020

@author: maf011
"""


class Rectangle:
   def __init__(self, length, breadth, unit_cost):
       self.length = length
       self.breadth = breadth        
       self.unit_cost = unit_cost
   def get_area(self):
       return self.length * self.breadth
   def calculate_cost(self):
       area = self.get_area()
       return area * self.unit_cost
   def perimeter(self, n ):     #n absurd, just for playing
       return (2* self.length + 2* self.breadth) * n
       
# breadth = 120 units, length = 160 units, 1 sq unit cost = Rs 2000
r = Rectangle(160, 120, 0.5)
print("Area of Rectangle: %s sq units" % (r.get_area()))

print("Cost: %s sq units" % (r.calculate_cost()))

print ('n times Perimeter: %s' % (r.perimeter(2)))