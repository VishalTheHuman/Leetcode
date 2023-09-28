# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ls = []
    def sumRootToLeaf(self, root: Optional[TreeNode],string="") -> int:
        sum_=0
        string += str(root.val)
        if root.left is None and root.right is None:
            return int(string,2)
        if root.left:
            sum_+=self.sumRootToLeaf(root.left,string)
        if root.right:
            sum_+=self.sumRootToLeaf(root.right,string)
        return sum_