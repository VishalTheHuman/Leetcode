# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        while q and root:
            lvlsum = 0
            for i in range(len(q)):
                node = q.popleft()
                lvlsum+=node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
        return lvlsum