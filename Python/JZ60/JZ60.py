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
        
        ret = []
        
        stack = [pRoot]
        size = 1
        while stack:
            a = []
            while size>0:
                p = stack.pop(0)
                a.append(p.val)
            
                if p.left != None:
                    stack.append(p.left)
                if p.right != None:
                    stack.append(p.right)

                size -= 1
                    
            ret.append(a)
            size = len(stack)
            
        return ret
