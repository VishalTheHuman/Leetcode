# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        self.ls = []
        def inorder(root):
            if not root: return []
            if root.left:
                inorder(root.left) 
            self.ls.append(root.val)
            if root.right:
                inorder(root.right)
        inorder(root1)
        inorder(root2)
        return sorted(self.ls)