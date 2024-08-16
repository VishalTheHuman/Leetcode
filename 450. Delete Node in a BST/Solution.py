# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left,key)
        elif key > root.val:
            root.right = self.deleteNode(root.right,key)
        else:
            if not root.left and not root.right:
                return None
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            
            curr = root.right
            while curr.left:
                curr = curr.left
            min_val = curr.val
            root.val = min_val
            root.right = self.deleteNode(root.right,min_val)
        return root