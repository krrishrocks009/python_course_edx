# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 16:23:27 2017

@author: kkesi
"""

months = 1
annualInterestRate = 0.2
balance = 3329
monthlyInterestRate = annualInterestRate / 12.0


while months <= 12:  
    if months == 1:
        minFixedMonthlyPayment = balance / 12
        monthlyUnpaid = balance - minFixedMonthlyPayment
    
    else:
        monthlyUnpaid = balance + (monthlyInterestRate * balance)
        updatedBalance = (monthlyUnpaid + (monthlyInterestRate * monthlyUnpaid))
        minFixedMonthlyPayment = updatedBalance / 12
    print(updatedBalance)
    if months == 12:
        
        print(' Lowest Payment: ' + str(minFixedMonthlyPayment))
    months += 1
