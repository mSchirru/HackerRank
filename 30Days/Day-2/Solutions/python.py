#!/bin/python3

import sys
def calculate(meal_cost, tip_percent, tax_percent):
    tip = meal_cost * (tip_percent/100)
    tax = meal_cost * (tax_percent/100)
    totalCost = float(meal_cost + tip + tax)
    print("The total meal cost is " + str(round(totalCost)) + " dollars.")
    

if __name__ == "__main__":
    meal_cost = float(input().strip())
    tip_percent = int(input().strip())
    tax_percent = int(input().strip())
    calculate(meal_cost, tip_percent, tax_percent)