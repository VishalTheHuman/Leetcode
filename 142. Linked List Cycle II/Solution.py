# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = set()
        i = 0
        while head:
            if head not in s:
                s.add(head)
                head = head.next
            else:
                return head
            i+=1
        return None