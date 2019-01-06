# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 18:25:04 2019

@author: Loqx
"""
# input the following variables
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))
# call the following variables for computation
portion_down_payment = 0.25
current_savings = 0
r = 0.04
monthly_salary = annual_salary / 12

# for LOOPS for monthly savings
for num in range(0, 300, 1):
    if current_savings > total_cost * portion_down_payment:
        print("Number of months:", num + 1)
        break
    else:
        if num % 6 == 0 and num != 0:
            monthly_salary = monthly_salary * (1 + semi_annual_raise)
        
        current_savings += (monthly_salary * portion_saved)
        current_savings = current_savings * (1 + r / 12)