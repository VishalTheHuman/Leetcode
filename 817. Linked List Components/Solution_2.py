# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        parts = 0
        link = False
        while head.next:
            if head.val in nums:
                link = True
            if link and head.val not in nums:
                link = False
                parts+=1
            head = head.next
        
        if head.val in nums or link:
            return parts+1

        return parts