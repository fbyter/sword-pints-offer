# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        l = len(A)
            
        B2 = list(range(l))
        B2[l-1] = 1
        for i in reversed(range(0, l-1)):
            B2[i] = B2[i+1] * A[i+1]
                    
        B = list(range(l))
        B[0] = 1
        for i in range(1, l):
            B[i] = B[i-1] * A[i-1]
        
        for i in range(l):
            B[i] =  B[i] * B2[i]

        return B
