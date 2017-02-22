# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 17:15:06 2017

@author: kkesi
"""

d1 = {1:30, 2:20, 3:30, 5:80}
d2 = {1:40, 2:50, 3:60, 4:70, 6:90}

def dict_interdiff(d1, d2):
    intersect = {}
    difference = {}
    for key in d1.keys():
        if key in d2.keys():
            intersect[key] = f(d1[key], d2[key])
        else:
            difference[key] = d1[key]
    
    for key in d2.keys():
        if not key in d1.keys():
            difference[key] = d2[key]
    return {{intersect}, {difference}}

print(dict_interdiff(d1, d2)) 