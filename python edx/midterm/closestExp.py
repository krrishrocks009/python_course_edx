# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 22:47:21 2017

@author: kkesi
"""

def closest_power2(base, num):
    exp=1
    while base**exp<=num:
        if base**exp <= num <= base**(exp+1):
           num_low = base**exp
           num_high = base**(exp+1)
           return exp if num-num_low<num_high-num else exp+1
        exp += 1
    return 0
print(closest_power2(2, 192.0))
        
        
        
        
        
        

        
        
         
        