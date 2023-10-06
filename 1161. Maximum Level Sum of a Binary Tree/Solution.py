# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_sum = root.val 
        max_level = 1
        q = deque([root])
        l = 1
        while q and root:
            s = 0
            for _ in range(len(q)):
                node = q.popleft()
                s+=node.val
                if node.left: 
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if s > max_sum:
                max_sum = s
                max_level = l
            l+=1
        return max_level