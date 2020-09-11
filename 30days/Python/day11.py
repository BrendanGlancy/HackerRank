#!/usr/bin/env python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    smax = -9 * 7

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))


    

        for row in range(len(arr) -2):
            for column in range(len(arr[row]) -2):
                tl = arr[row][column]
                tc = arr[row][column + 1]
                tr = arr[row][column + 2]
                mc = arr[row + 1][column + 1]
                bl = arr[row + 2][column]
                bc = arr[row + 2][column + 1]
                br = arr[row + 2][column + 2]
                s = tl + tc + tr + mc + bl + bc + br
                smax = max(s, smax)

print(smax)
