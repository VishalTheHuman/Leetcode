# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.sum_ = 0
        self.dfs(root)
        return self.sum_
    
    def dfs(self,root):
        if not root: return
        if root.val % 2 == 0:
            if root.left and root.left.left: self.sum_+=root.left.left.val
            if root.left and root.left.right: self.sum_+=root.left.right.val 
            if root.right and root.right.left: self.sum_+=root.right.left.val
            if root.right and root.right.right: self.sum_+=root.right.right.val  
        self.dfs(root.right)
        self.dfs(root.left)