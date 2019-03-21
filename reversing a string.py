# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 11:05:23 2019

@author: adminsystem
"""
class rev:
 def leng(self,string):
     self.string=string
     n=len(string)
 def str(string):
    if len(string) == 0:
        return string
    else:
        return str (string[n]) + string[1:]
r=rev()    
string = input()
print(str(string))
