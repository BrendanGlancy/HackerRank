#!/usr/bin/env python3

import math
import os
import random
import re
import sys

n = int(input().strip())
# Complete the factorial function below.


def _factorial(N):
    if N <= 1:
        return 1
    return N * _factorial(N - 1)

def factorial(N):
    print(_factorial(N))




if __name__ == '__main__':
    factorial(n)
