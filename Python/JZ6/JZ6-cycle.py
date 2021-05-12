# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        
        # 1. array is empty
        if rotateArray==None or len(rotateArray)==0:
            return 0

        # 2.
        i=0
        while i < len(rotateArray)-1:
            if rotateArray[i] > rotateArray[i+1]:
                return rotateArray[i+1]
            i+=1

        return rotateArray[0]

        