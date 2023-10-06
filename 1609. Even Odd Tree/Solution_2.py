# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        lvl = 0
        q = deque([root])
        while root and q:
            prev = 1000000 if lvl % 2  else 0
            for _ in range(len(q)):
                node = q.popleft() 
                if lvl%2:
                    if node.val <prev and node.val%2==0:
                        prev = node.val
                    else:
                        return False
                else:
                    if node.val >prev and node.val%2==1:
                        prev = node.val
                    else:
                        return False
                    
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            lvl+=1
        return True