# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 00:12:31 2019

@author: Loqx
"""


def cal_savings(guess):
    current_savings = 0
    r = 0.04
    monthly_salary = annual_salary / 12
    semi_annual_raise = 0.07
    for num in range(0,36):
        if num % 6 == 0 and num != 0:
            monthly_salary = monthly_salary * (1 + semi_annual_raise)
        
        current_savings += (monthly_salary * guess)
        current_savings = current_savings * (1 + r / 12)
    print("Current savings", current_savings)
    return current_savings


annual_salary = int(input("Enter annual salary:"))
guess = float(input("Enter guess rate:"))
cal_savings(guess)