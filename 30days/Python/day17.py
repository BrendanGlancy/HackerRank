#!/usr/bin/env python3

class Calculator(object):
    def power(self, n, p):
        if (n < 0) or (p < 0):
            raise Exception("n and p should be non-negative")
        else:
            return n ** p
