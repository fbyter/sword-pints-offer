# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        ret = [0] * 58
        for c in s:
            ret[ord(c)-65] += 1

        for i in range(len(s)):
            if ret[ord(s[i])-65]==1:
                return i
                
        return -1