# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if root == None:
            return []
        
        stack = [root]
        ret = []
        while stack:
            p = stack.pop(0)
            ret.append(p.val)
            
            if p.left != None:
                stack.append(p.left)
            if p.right != None:
                stack.append(p.right)
            
        return ret