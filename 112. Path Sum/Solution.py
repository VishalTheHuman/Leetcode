# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int,sum_:int = 0) -> bool:
        if not root: return False
        if not root.right and not root.left:
            return True if root.val + sum_ == targetSum else False
        val = root.val + sum_
        l = self.hasPathSum(root.right,targetSum,val)
        r = self.hasPathSum(root.left,targetSum,val)
        return l or r