# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 18:25:04 2019

@author: Loqx
"""


def cal_savings(guess):
    current_savings = 0
    r = 0.04
    monthly_salary = annual_salary / 12
    semi_annual_raise = 0.07
    for num in range(0, 36):
        if num % 6 == 0 and num != 0:
            monthly_salary = monthly_salary * (1 + semi_annual_raise)
        current_savings += (monthly_salary * guess)
        current_savings = current_savings * (1 + r / 12)
    print("Current savings", current_savings)
    return current_savings


# input the following variables
annual_salary = float(input("Enter your starting salary: "))

# call the following variables for computation
portion_down_payment = 0.25
total_cost = 1000000
epsilon = 100
current_savings = 0
# low and high boundary
num_guesses = 0
low = 0.00
high = 1.00
guess = (low + high) / 2.0
   
while abs(current_savings - total_cost * portion_down_payment) >= epsilon:
    if current_savings > total_cost * portion_down_payment:
        low = guess
    else:
        high = guess
    guess = (low + high) / 2.0
    num_guesses += 1
    current_savings = 251000 - 100 * num_guesses
    
print("Best savings rate:", guess)
print("Steps in bisection search", num_guesses)
