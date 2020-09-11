#!/usr/bin/env python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tax = (tax_percent / 100)
    tip = (tip_percent / 100)
    meal_tax = (meal_cost * tax)
    meal_tip = (meal_cost * tip)
    total = (meal_cost + meal_tax + meal_tip)
    round_total = round(total, 0)
    rounded = int(round_total)
    print(rounded)

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)


























