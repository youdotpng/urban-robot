# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 02:57:21 2017

@author: nicol
"""
from SQ_classes import *


class seq_math(stack):
    def solve_problem(self):
        err_check = False
        self.prbm = input("Please enter the prefix operation to be solved: ")
        for char in self.prbm.split():
            if char.isdigit():
                self.push(int(char))
            else:
                err_check = self.operation_choice(char)
        if err_check:
            while (self.pop() is not None):
                self.pop()
            return
        while(len(self.content) > 1):
            self.operation_choice('*')
        print("The answer is", self.pop())

    def operation_choice(self, sym):
        if len(self.content) <= 1:
            print("Too many operations were entered")
            return True
        if sym == '+':
            temp = self.pop()
            temp += self.pop()
            self.push(temp)
            return
        elif sym == '-':
            temp = self.pop()
            temp += self.pop()
            self.push(temp)
            return
        elif sym == '*':
            temp = self.pop()
            temp *= self.pop()
            self.push(temp)
            return
        elif sym == '/' or sym == '\\':
            temp = self.pop()
            temp /= self.pop()
            self.push(temp)
            return
        else:
            print("Please only use +, -, *, or /")
            return True
