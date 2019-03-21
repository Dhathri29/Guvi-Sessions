# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 15:17:52 2019

@author: adminsystem
"""

input_list = [10,1,2,11]
for i in range(len(input_list)): 
    for j in range(i):    
     if int(input_list[j]) > int(input_list[j+1]):     
        input_list[j],input_list[j+1] = input_list[j+1],input_list[j]
print (input_list)
