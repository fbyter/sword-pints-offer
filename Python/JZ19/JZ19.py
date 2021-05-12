# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here

        if len(matrix) == 0:
            return []

        ret = matrix.pop(0) #取第一行
        while matrix:
            # 左旋矩阵
            m = []
            line = len(matrix) #行数
            column = len(matrix[0]) #列数
            for y in reversed(range(column)):
                mm = []
                for x in range(line):
                    mm.append(matrix[x][y])
                m.append(mm)
            
            ret += m.pop(0) #取第一行

            matrix = m

        return ret

