#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
for num in range(10,20):  # iterate the number from 10 to 20 
   for i in range(2,num): # iterate according to the factor
      if num%i == 0:      # get the first factor
         j=num/i          # calculate the second factor
         print '%d 等于 %d * %d' % (num,i,j)
         break            # jump out of the current circle
   else:                  # "else" section of the circle
      print num, 'it is a prime number'
