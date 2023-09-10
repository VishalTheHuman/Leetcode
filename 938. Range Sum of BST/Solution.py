# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root:
            if root.val<low:
                return self.rangeSumBST(root.right, low, high)
            elif root.val>high:
                return self.rangeSumBST(root.left, low, high)
            if root.val>=low and root.val<=high:
                return root.val + self.rangeSumBST(root.right, low, high) + self.rangeSumBST(root.left, low, high)
        return 0