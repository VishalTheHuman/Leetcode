# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        visited = set()
        result = False
        def dfs(node):
            nonlocal result,k
            if not node or result:
                return
            visited.add(node.val)
            if k - node.val in visited and (k-node.val)!=node.val:
                result = True
                return
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return result
