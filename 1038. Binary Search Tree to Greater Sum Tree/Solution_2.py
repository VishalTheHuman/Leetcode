# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        elements = self.inorder(root)
        max_val = max(elements)
        sum_val = sum(elements)
        q = deque([root])
        while root and q:
            for i in range(len(q)):
                node = q.popleft()
                if node.val != max_val:
                    node.val = sum(elements[elements.index(node.val):])
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
        return root
    
    def inorder(self,root):
        el = []
        if root.left:
            el+=self.inorder(root.left)
        el.append(root.val)
        if root.right:
            el+=self.inorder(root.right)
        return el