# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None and root2 is None:
            return None
        r1 = root1.val if root1 else 0
        r2 = root2.val if root2 else 0 
        node = TreeNode(r1+r2) 
        node.left = self.mergeTrees(root1.left if root1 else None ,root2.left if root2 else None)
        node.right = self.mergeTrees(root1.right if root1 else None ,root2.right if root2 else None)
        return node
