# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.convert(root,0)
        return root
    def convert(self,root,sum_val):
        if root:
            if root.right is None:
                root.val+=sum_val
            else:
                root.val += self.convert(root.right,sum_val)
            if root.left is None:
                return root.val
            else:
                return self.convert(root.left,root.val)