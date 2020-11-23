# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if pRoot == None:
            return []
        
        stack = [pRoot]
        size = 1
        ret = []
        while stack:
            a = []
            for i in range(size):
                p = stack.pop(0)
                a.append(p.val)
            
                if p.left != None:
                    stack.append(p.left)
                if p.right != None:
                    stack.append(p.right)
                    
            ret.append(a)
            size = len(stack)
            
        return ret