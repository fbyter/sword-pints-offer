# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stackIn = []
        self.stackOut = []

    def push(self, node):
        self.stackIn.append(node)

    def pop(self):
        # if array ->  array.noEmpty
        if self.stackOut:
            return self.stackOut.pop()
        elif self.stackIn:
            while self.stackIn:
                self.stackOut.append(self.stackIn.pop())
            return self.stackOut.pop()
        else:
            return None
