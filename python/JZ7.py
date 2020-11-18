# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            r=[0,1]
            for i in range(2,n+1):
                r.append(r[i-2] + r[i-1])
                
            return r[n]