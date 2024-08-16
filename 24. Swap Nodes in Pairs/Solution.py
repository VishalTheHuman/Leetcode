# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        if not head.next:
            return head
        
        node1 = head
        node2 = head.next

        node1.next = self.swapPairs(node2.next)
        node2.next = node1
        
        return node2