# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 17:05:35 2017

@author: nicol
"""


class queue:
    def __init__(self, data=[]):
        self.content = []
        for d in data:
            self.content.append(d)

    def enQ(self, data):
        for d in data:
            self.content.append(d)

    def deQ(self):
        if self.content == []:
            return None
        return self.content.pop(0)

    def size(self):
        return len(self.content)

    def __str__(self):
        str_version = ""
        for d in self.content:
            str_version += d

        return str_version

    def peek(self):
        if self.content == []:
            return None
        return self.content[0]


class stack:
    def __init__(self, data=[]):
        self.content = []
        for d in data:
            self.content.append(d)

    def __str__(self):
        str_version = ""
        for item in self.content:
            str_version += item
        return str_version

    def push(self, data):
        for d in data:
            self.content.append(d)

    def pop(self):
        return self.content.pop()

    def peek(self):
        return self.content[0]

    def size(self):
        return len(self.content)
