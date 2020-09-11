#!/usr/bin/env python3

class Person:
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        if initialAge < 0:
            print('Age is not valid, setting age to 0.')
            self._age = 0
        else:
            self._age = initialAge

    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if self._age < 13:
            print('You are young.')
        elif (self._age) and (self._age < 18):
            print('You are a teenager.')
        else:
            print('You are old.')
        
    def yearPasses(self):
        # Increment the age of the person in here
        self._age += 1
