#!/usr/bin/env python3

class Solution(object):
    
    def __init__(self):
        self.__stack = []
        self.__queue = []

    def pushCharacter(self, ch):
        self.__stack.append(ch)

    def enqueueCharacter(self, ch):
        self.__queue.insert(0, ch)

    def popCharacter(self):
        return self.__stack.pop()

    def dequeueCharacter(self):
        return self.__queue.pop()
