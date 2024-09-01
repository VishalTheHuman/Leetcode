# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int,ls = []) -> List[List[int]]:
        result = []
        def dfs(node, pathSum = 0, arr = []): 
            nonlocal targetSum

            pathSum += node.val
            arr.append(node.val)
            
            if node.left:
                dfs(node.left, pathSum , arr)
            if node.right:
                dfs(node.right, pathSum, arr)
            
            if not node.right and not node.left: 
                if pathSum == targetSum: 
                    result.append(arr.copy())
                
            arr.pop()
        if root:
            dfs(root)
        return result
