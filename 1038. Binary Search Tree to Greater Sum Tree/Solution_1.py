# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def convert(root,sum_val):
            if root.right is None:
                root.val+=sum_val
            else:
                root.val += convert(root.right,sum_val)

            if root.left is None:
                return root.val
            else:
                return convert(root.left,root.val)
        convert(root,0)
        return root