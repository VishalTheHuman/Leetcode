# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root):
        return (self.getHeight(root) >= 0)
    def getHeight(self, root):
        if root is None:  return 0
        leftheight, rightheight = self.getHeight(root.left), self.getHeight(root.right)
        if leftheight < 0 or rightheight < 0 or abs(leftheight - rightheight) > 1:  return -1
        return max(leftheight, rightheight) + 1