# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if None==pre or len(pre)==0:
            return None
        
        rootVal = pre[0]
        root = TreeNode(rootVal)

        tinIndex = tin.index(rootVal)
        preIndex=0
        for i in tin[0:tinIndex]:
            current = pre.index(i)
            if current > preIndex:
                preIndex = current
            
        root.left = self.reConstructBinaryTree(pre[1:preIndex+1], tin[:tinIndex])
        root.right = self.reConstructBinaryTree(pre[preIndex+1:], tin[tinIndex+1:])
        
        return root
