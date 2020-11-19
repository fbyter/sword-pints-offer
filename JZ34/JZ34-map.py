# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        m = {}
        order = 0
        for i in range(len(s)):
            key = s[i]
            if key not in m:
                m[key] = [1, order, i]
                order += 1
            else:
                m[key][0] += 1
                
        ret = -1
        currentOrder = 10001
        for key in m:
            if m[key][0]==1 and m[key][1]<currentOrder:
                ret = m[key][2]
                currentOrder = m[key][1]
                
        return ret