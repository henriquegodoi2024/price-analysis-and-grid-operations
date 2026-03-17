# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def repeat(s, n):
    ''' creates a string in which n copies of s have been
    concatenated'''
    new = ''
    if n <= 0:
        return new
    for i in range(n):
        new += s   
    return new

def contains(s,c):
    ''' checks if s is in c using a loop'''
    for r in s:
        if r == c:
            return True
    return False

    
def add(vals1,vals2):
    
    ''' uses an index based loop to create a list that is the sum of
    the element in vals1 and vals2 in their respective positions'''
    if len(vals1) < len(vals2):
      vals1 = [0] * (len(vals2) - len(vals1)) + vals1
      
    elif len(vals2) < len(vals1):
      vals2 = [0] * (len(vals1) - len(vals2)) + vals2
    
       
    result = []    
    for i in range(len(vals1)):
        result += [vals1[i] + vals2[i]]
    
    return result
          

def replace(vals,old,new):
    ''' modifies the list vals by replacing occurences of old with 
    new'''
    for i in range(len(vals)):
        if vals[i] == old:
            vals[i] = new
            


