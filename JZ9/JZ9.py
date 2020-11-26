# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number<=0:
            return 0
        elif number==1:
            return 1
        
        else:
            return 2* self.jumpFloorII(number-1)