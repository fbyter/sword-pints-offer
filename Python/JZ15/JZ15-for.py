# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if pHead==None or pHead.next==None:
            return pHead
        
        p = pHead
        pNext = p.next
        p.next = None
        
        while pNext!=None:
            pTemp = pNext.next
            pNext.next = p
            
            p = pNext
            pNext = pTemp
            
        return p