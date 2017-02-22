# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 18:18:01 2017

@author: kkesi
"""

def f(i):
    return i + 2
def g(i):
    return i > 5

def applyF_filterG(L, f, g):
    
    copied_L = L[:]
    for i in copied_L:
        if not g(f(i)):
            L.remove(i)
    if len(L)==0:
        return -1
    else:
        return  max(L)

    

    
    
    

L = [0, -10, 5, 6, -4]
print(applyF_filterG(L, f, g))
print(L)   