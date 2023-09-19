# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(val=preorder[0])
        for elem in preorder[1:]:
            self.buildTree(root,elem)
        return root
    
    def buildTree(self,root,val):
        if val<root.val:
            if root.left:
                self.buildTree(root.left,val)
            else:
                root.left = TreeNode(val)
        else:
            if root.right:
                self.buildTree(root.right,val)
            else:
                root.right = TreeNode(val)