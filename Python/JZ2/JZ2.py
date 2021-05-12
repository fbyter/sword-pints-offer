# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        l = len(s)
        i = 0
        st = ''
        while i<l:
            if s[i]==' ':
                st += '%20'
            else:
                st += s[i]

            i += 1

        return st
