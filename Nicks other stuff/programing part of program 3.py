# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 17:25:09 2017

@author: nicol
"""

from SQ_classes import *


class new_queue:
    def __init__(self, data=[]):
        self.S1 = stack(data)
        self.S2 = stack()

    def __str__(self):
        ret_str = ""
        while (self.S1.size() > 0):
            self.S2.push(self.S1.pop())
        while (self.S2.size() > 0):
            self.S1.push(self.S2.pop())
            ret_str = ret_str + str(self.S1.peek()) + " " 
        return ret_str

    def deQ(self):
        while(self.S1.size() > 1):
            self.S2.push(self.S1.pop())
        value = self.S1.pop()
        while (self.S2.size() > 0):
            self.S1.push(self.S2.pop())
        return(value)

    def enQ(self, data):
        self.S1.push(data)

    def size(self):
        return(self.S1.size())

    def peek(self):
        while(self.S1.size() > 1):
            self.S2.push(self.S1.pop())
        value = self.S1.peek()
        self.S2.push(self.S1.pop())
        while (self.S2.size() > 0):
            self.S1.push(self.S2.pop())
        return(value)


class new_stack:
    def __init__(self, data=[]):
        self.Q1 = queue(data)
        self.Q2 = queue()

    def __str__(self):
        ret_str = ""
        while (self.Q1.size() > 0):
            ret_str = str(self.Q1.peek()) + " " + ret_str
            self.Q2.enQ(self.Q1.deQ())
        while (self.Q2.size() > 0):
            self.Q1.enQ(self.Q2.deQ())
        return ret_str

    def push(self, data):
        self.Q1.enQ(data)

    def pop(self):
        while(self.Q1.size() > 1):
            self.Q2.enQ(self.Q1.deQ())
        value = self.Q1.deQ()
        while(self.Q2.size() > 0):
            self.Q1.enQ(self.Q2.deQ())
        return(value)

    def size(self):
        return(self.Q1.size())

    def peek(self):
        while(self.Q1.size() > 1):
            self.Q2.enQ(self.Q1.deQ())
        value = self.Q1.peek()
        self.Q2.enQ(self.Q1.deQ())
        while(self.Q2.size() > 0):
            self.Q1.enQ(self.Q2.deQ())
        return(value)

def main():
    print("queue")
    a = new_queue()
    b = new_stack()
    for j in range(50):
        i = j*2
        a.enQ(i)
        b.push(i)
    print(a)
    print(a.deQ())
    print(a.peek())
    print(a.size())
    print(a)
    
    print("stack")
    print(b)
    print(b.pop())
    print(b.peek())
    print(b.size())
    print(b)

if __name__ == '__main__':
    main()

