# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        low=0; high = len(array)-1
        while low<high:
            sumx = array[low]+array[high]
            if sumx < tsum:
                low += 1
            elif sumx > tsum:
                high -= 1
            else:
                return [array[low], array[high]]
            
        return []