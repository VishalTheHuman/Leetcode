# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        parts = 0
        while head:
            while head and head.val not in nums:
                head = head.next
            parts += head is not None
            while head and head.val in nums:
                head = head.next
        return parts