#!/usr/bin/env python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    
    list.reverse(arr)
    
    for i in range(n):
        print(arr[i], end =" ")
