# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        
        # 1. array is empty
        if rotateArray==None or len(rotateArray)==0:
            return 0

        # 2.
        low = 0
        high = len(rotateArray) - 1
        middle = 0
        # 旋转数组低位大于高位
        while rotateArray[low] >= rotateArray[high]:
            if(low == high-1):
                middle = high
                break
            else:
                middle = low + (high-low)//2
                # middle大于low，[low,middle]是顺序增长，从[middle,high]查找
                if(rotateArray[middle] >= rotateArray[low]):
                    low = middle
                # middle小于high，[middle,high]是顺序增长，从[low,middle]查找
                if(rotateArray[middle] <= rotateArray[high]):
                    high = middle

        return rotateArray[middle]
