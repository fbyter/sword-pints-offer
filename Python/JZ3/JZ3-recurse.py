# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]

    def printListFromTailToHead(self, listNode):
        # write code here
        if listNode != None:
            ret = self.printListFromTailToHead(listNode.next)
            ret.append(listNode.val)
            return ret
        else :
            return []

"""
    这个方法使用全局变量, 导致并发测试有问题
    ret = []
    def printListFromTailToHead(self, listNode):
        # write code here
        if listNode != None:
            self.printListFromTailToHead(listNode.next)
            self.ret.append(listNode.val)
        
        return self.ret
"""
