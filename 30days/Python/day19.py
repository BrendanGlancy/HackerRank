#!/usr/bin/env python3

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        val = 0
        for i in range(1, n+1):
            if(n % i ==0):
                val += i
        return val
