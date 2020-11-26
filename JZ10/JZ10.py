# -*- coding:utf-8 -*-
class Solution:
    # fn = f(n-1) + f(n-2)
    def rectCover(self, number):
        # write code here
        if number<=0:
            return 0
        elif number==1:
            return 1
        elif number==2:
            return 2
        else:
            array = [1,2]
            i=2
            while i<number:
                array.append(array[i-1] + array[i-2])
                i += 1
            return array[number-1]