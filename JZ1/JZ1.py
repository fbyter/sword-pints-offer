# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        row = len(array)
        if row==0:
            return False

        col = len(array[0])
        x = 0; y=col-1

        while x<row and y>=0:
            n = array[x][y]
            if n < target:
                x += 1
            elif n > target:
                y -= 1
            else:
                return True

        return False