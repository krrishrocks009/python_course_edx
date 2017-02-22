# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 18:12:12 2017

@author: kkesi
"""

def genPrimes():
    primes = []   
    last = 1      
    while True:
        last += 1
        for p in primes:
            if last % p == 0:
                break
        else:
            primes.append(last)
            yield last