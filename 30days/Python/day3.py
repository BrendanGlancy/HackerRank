#!/usr/bin/env python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    if N >= 2 and N <=5 and N % 2 == 0:
        print('Not Weird')
    elif N % 2 != 0:
        print('Weird')

    elif N >= 6 and N <= 20 and N % 2 == 0:
        print('Weird')
    elif N % 2 != 0:
        print('Not Weird')

    elif N > 20 and N % 2 == 0:
        print('Not Weird')
    elif N % 2 != 0:
        print('Weird')
