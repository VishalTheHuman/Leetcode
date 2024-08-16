# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode],string="") -> int:
        def dfs(node,curr_sum):
            if not node:
                return 0
            curr_sum = (curr_sum << 1) | node.val
            if not node.left and not node.right:
                return curr_sum
            ls = dfs(node.left,curr_sum)
            ls += dfs(node.right,curr_sum)
            return ls
        return dfs(root,0)