# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    # 超时
    def Find(self, target, array):
        # write code here
        for line in array:
            low=0; high=len(line)
            while low <= high:
                mid=(low+high)//2
                if target < line[mid]:
                    high = mid
                elif target > line[mid]:
                    low = mid
                else:
                    return True

        return False