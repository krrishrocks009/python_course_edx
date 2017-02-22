# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 02:23:37 2017

@author: kkesi
"""

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    return sum([listA[i] * listB[i] for i in range(len(listA))])
print(dotProduct([1 ,2, 3], [1, 2, 3])) 