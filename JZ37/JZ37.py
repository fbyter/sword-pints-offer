# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        if not data:
            return 0
        
        return self.biSearchLast(data, k) - self.biSearchFirst(data, k)

    def biSearchFirst(self, data, k):
        index = self.biSearch(data, k)
        if index>=0 and index<len(data) and data[index]==k:
            while (index-1)>=0 and data[index-1]==k:
                index -= 1
            return index
        else:
            return index

    def biSearchLast(self, data, k):
        l = len(data)
        index = self.biSearch(data, k)
        if index>=0 and index<l and data[index]==k:
            while (index+1)<l and data[index+1]==k:
                index += 1
            return index+1
        else:
            return index
    
    def biSearch(self, data, k):
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