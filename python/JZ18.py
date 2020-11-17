# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#
# 
# @param pRoot TreeNode类 
# @return void
#
class Solution:
    def Mirror(self , pRoot ):
        # write code here
        if(pRoot == None):
            return

        if(pRoot.left==None and pRoot.right==None):
            return

        # switch left and right child
        pMid = pRoot.left
        pRoot.left = pRoot.right
        pRoot.right = pMid

        self.Mirror(pRoot.left)
        self.Mirror(pRoot.right)
