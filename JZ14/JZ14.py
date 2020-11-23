# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if head==None or k<=0:
            return None
        
        p1 = head
        i = 0
        while i<k:
            if p1==None:
                return None
            p1 = p1.next
            i += 1
        
        p2 = head
        while p1!=None:
            p1 = p1.next
            p2 = p2.next
            
        return p2