# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 17:05:35 2017

@author: nicol
"""


class queue:
    def __init__(self, data=[]):
        self.content = []
        if type(data) == list:
            for d in data:
                self.content.append(d)
        else:
            self.content.append(data)

    def __str__(self):
        str_version = ""
        for d in self.content:
            str_version += "{} ".format(str(d))
        return str_version

    def enQ(self, data):
        if type(data) == list:
            for d in data:
                self.content.append(d)
        else:
            self.content.append(data)

    def deQ(self):
        if self.content == []:
            return None
        return self.content.pop(0)

    def size(self):
        return len(self.content)

    def peek(self):
        if self.content == []:
            return None
        return self.content[0]


class stack:
    def __init__(self, data=[]):
        self.content = []
        if type(data) == list:
            for d in data:
                self.content.append(d)
        else:
            self.content.append(data)

    def __str__(self):
        str_version = ""
        for d in self.content:
            str_version += "{} ".format(str(d))
        return str_version

    def push(self, data):
        if type(data) == list:
            for d in data:
                self.content.append(d)
        else:
            self.content.append(data)

    def pop(self):
        if self.content == []:
            return None
        return self.content.pop()

    def peek(self):
        return self.content[-1]

    def size(self):
        return len(self.content)
