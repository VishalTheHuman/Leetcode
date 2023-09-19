# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        deep_lvl = self.getDeepLevel(root,0)
        self.ls = []
        self.sum_tree(root,0,deep_lvl)
        return sum(self.ls)
    
    def sum_tree(self,root,lvl,deep):
        if root:
            if lvl == deep-1:
                self.ls.append(root.val)
            self.sum_tree(root.left,lvl+1,deep)
            self.sum_tree(root.right,lvl+1,deep)
    
    def getDeepLevel(self,root,lvl):
        if not root: return lvl
        lvl+=1
        return max(self.getDeepLevel(root.right,lvl),self.getDeepLevel(root.left,lvl))   