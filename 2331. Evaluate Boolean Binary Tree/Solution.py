# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root: return
        if root.left is None and root.right is None:
            return True if root.val == 1 else False
        
        if root.val == 2:
            return self.evaluateTree(root.right) or self.evaluateTree(root.left)
        else:
            return self.evaluateTree(root.right) and self.evaluateTree(root.left)