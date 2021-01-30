# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        if base==0:
            return 0
        elif exponent==0:
            return 1
        else:
            ret=1
            for i in range(abs(exponent)):
                ret *= base

            return ret if exponent>0 else 1.0/ret
