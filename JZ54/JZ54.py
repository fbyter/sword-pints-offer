# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    def __init__(self):
        self.n = 1
        self.count = []
        for i in range(256):
            self.count.append([0,0])
    def FirstAppearingOnce(self):
        # write code here
        ret = '#'
        min = 257
        for i in range(256):
            if self.count[i][0]==1 and self.count[i][1]<min:
                min = self.count[i][1]
                ret = chr(i)
        return ret

    def Insert(self, char):
        # write code here
        index = ord(char)
        if self.count[index][1] == 0:
            self.count[index][1] = self.n
            self.n += 1
        self.count[index][0] += 1
