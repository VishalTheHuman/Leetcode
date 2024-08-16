# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.ls = [0]
        root.val = 0
        self.recover(root,0)

    def recover(self,root,parent):
        l = 0
        r = 0
        if not root: return root
        if root.left:
            l = 2*parent + 1
            self.ls.append(l)
        if root.right:
            r = 2*parent + 2
            self.ls.append(r)
        
        self.recover(root.left,l)
        self.recover(root.right,r)
        return root

    def find(self, target: int) -> bool:
        return target in self.ls


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)