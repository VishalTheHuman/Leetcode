# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        prev, slow, fast = None, head, head
        max_val = 0

        while fast:
            fast = fast.next.next
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        
        while slow:
            if prev.val + slow.val > max_val:
                max_val = prev.val + slow.val
            slow = slow.next
            prev = prev.next
        
        return max_val