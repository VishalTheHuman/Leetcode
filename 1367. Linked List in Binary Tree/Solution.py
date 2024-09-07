# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        doesExist = False
        def find(node, itr):
            nonlocal doesExist
            if not itr:
                doesExist = True
                return
            if not node or node.val != itr.val or doesExist: 
                return 
            
            find(node.left, itr.next)
            find(node.right, itr.next)
        
        def solve(node):
            nonlocal doesExist
            if not node or doesExist: 
                return
            
            if node.val == head.val: 
                find(node, head)
            
            solve(node.left)
            solve(node.right)

        solve(root)
        return doesExist
