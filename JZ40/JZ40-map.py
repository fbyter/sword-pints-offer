# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here

        countMap = {}
        for key in array:
            if key in countMap: #countMap.keys
                countMap[key] += 1
            else:
                countMap[key] = 1

        ret = []
        for key in countMap:
            if countMap[key] == 1:
                ret.append(key)

        return ret

        
        