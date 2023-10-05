# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        count = 0
        while root and q:
            count+=len(q)
            for _ in range(len(q)):
                n = q.popleft()
                if n.right:
                    q.append(n.right)
                if n.left:
                    q.append(n.left)
        return count