# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        val = root.val
        q = deque([root])
        while q and root:
            for _ in range(len(q)):
                node = q.popleft()
                if node.val!=val:
                    return False
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right) 
        return True