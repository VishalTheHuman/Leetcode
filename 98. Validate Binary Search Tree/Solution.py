# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        result = True
        def validate(node):
            nonlocal result

            lMin = lMax = rMin = rMax = node.val

            if node.left:
                lMin, lMax = validate(node.left)
                if not result: return None, None
                if lMax >= node.val:
                    result = False
                    return None, None

            if node.right:
                rMin, rMax = validate(node.right)
                if not result: return None, None
                if rMin <= node.val:
                    result = False
                    return None, None

            left = right = node.val
            if node.left: 
                left =  lMin
            if node.right:
                right =  rMax
            return left, right
            
        validate(root)
        return result
