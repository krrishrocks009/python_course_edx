# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 14:54:14 2017

@author: kkesi
"""

months = 1
monthlyInterestRate = annualInterestRate / 12.0
minMonthlyPayment = monthlyPaymentRate * balance
total = 0

while months <= 12:  
    if months == 1:
        # Handling the special case when months = 1 and updatedBalance 
        # is not yet initialized
        minMonthlyPayment = round(monthlyPaymentRate * balance, 2) 
        monthlyUnpaid = balance - minMonthlyPayment
    else:  
        minMonthlyPayment = round(monthlyPaymentRate * updatedBalance, 2)
        monthlyUnpaid = updatedBalance - minMonthlyPayment 
               
    updatedBalance = round((monthlyUnpaid + (monthlyInterestRate * monthlyUnpaid)), 2)
    total += minMonthlyPayment
    
    print('Month: ' + str(months))
    print('Minimum monthly payment: ' +  str(minMonthlyPayment))
    print('Remaining balance: ' + str(updatedBalance))
    if months == 12:
        print('Total paid: ' + str(total))
        print('Remaining Balance: ' + str(updatedBalance))
    months += 1