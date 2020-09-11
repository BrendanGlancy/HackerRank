#!/usr/bin/env python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())



for i in range(1, 11):
    product = n * i 
    num1 = str(i)
    num2 = str(product)
    num3 = str(n)
    str1 = ' x '
    str2 = ' = '
    print(num3 + str1 + num1 + str2 + num2)
