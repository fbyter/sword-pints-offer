# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        duplication[0] = -1
        l = len(numbers)
        ary = [0]*l
        for i in numbers:
            ary[i] += 1
            if ary[i] > 1:
                duplication[0] = i
                return True
            
        return False
        
                