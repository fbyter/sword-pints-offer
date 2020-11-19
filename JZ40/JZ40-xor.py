# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here

        xor = 0
        for i in array:
            xor ^= i

        # xor=a^b, flag是(a^b)最低不相同位
        flag=1
        while (xor&flag)==0:
            flag <<= 1
        print(xor, flag)
        
        a1=0; a2=0
        for i in array:
            if (i&flag)==0:
                a1 ^= i
            else:
                a2 ^= i

        return [a1,a2]
