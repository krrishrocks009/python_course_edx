# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 18:11:02 2017

@author: kkesi
"""



def remaining_balance():
    result = 1
    while result > 0 and result >=12:
        MIR = (0.18)/12.0
        MMP = (0.02) * (5000)
        MUB = (5000) - (100)
        UBEM = (MUB) + (MIR * MUB)
        return MUB
    result += 1
print(remaining_balance())

