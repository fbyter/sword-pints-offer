# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        f=1
        ret=0
        if f&n == f:
            ret += 1
        for i in range(1,32):
            f <<= 1
            if f&n == f:
                ret += 1
                
        return ret