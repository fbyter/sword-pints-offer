# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        if s==None or s=='':
            return s
        
        l = len(s)
        n = n%l
        return s[n:] + s[:n]