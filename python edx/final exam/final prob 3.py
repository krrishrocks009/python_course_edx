# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 12:59:48 2017

@author: kkesi
"""

trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
          '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}
          
def convert_to_mandarin(us_num):
    
 
    if int(us_num) <= 10:
        res = trans[us_num]
        return res
        
    elif int(us_num) <= 19:
        res1 = trans['10']  + ' ' + trans[us_num[-1]]
        return res1
    
    elif int(us_num) <= 99:
        if int(us_num[-1]) == 0:
            res2 = trans[us_num[0]]+' '+trans['10']
            return res2
        else:
            res3 = trans[us_num[0]] +' '+ trans['10'] +' '+ trans[us_num[-1]]
            return res3
        
        