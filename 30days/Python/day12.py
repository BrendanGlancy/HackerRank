#!/usr/bin/env python3

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    

    
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores

    def calculate(self):
        a = sum(self.scores) / len(self.scores)
        if a < 40:
            return 'T'
        elif (a >= 40) and (a < 55):
            return "D"
        elif (a >= 55) and (a < 70):
            return 'P'
        elif (a >= 70) and (a < 80):
            return 'A'
        elif (a >= 80) and (a < 90):
            return 'E'
        elif (a >= 90) and (a <= 100):
            return 'O'
        else:
            return ''
        
        

        
    #   Return: A character denoting the grade.
    #
    # Write your function here
