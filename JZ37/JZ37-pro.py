# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        if not data:
            return 0
        
        return self.binarySearch(data, k+0.5) - self.binarySearch(data, k-0.5)
        
    def binarySearch(self, data, k):
        low=0; high=len(data)-1
        while low <= high: # <=
            mid = (low+high) >> 1
            midN = data[mid]
            if midN < k:
                low = mid+1 # mid+1
            elif midN > k:
                high = mid-1 # mid-1
            else:
                return mid
        
        #low always is the first number which > k 
        return low 