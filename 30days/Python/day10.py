#!/usr/bin/env python3

import math
import os
import random
import re
import sys

n = int(input())

count = 0
amt = 0

while n > 0:
    if n % 2 == 1:
        count += 1
        if count > amt:
            amt = count
    else:
        count = 0
    n //= 2
print(amt)
