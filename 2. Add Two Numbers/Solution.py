# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = ListNode(0)
        itr = head
        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            carry,val = (v1+ v2 + carry)//10, (v1+ v2 + carry)%10
            itr.next = ListNode(val)
            itr = itr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        if carry:
            itr.next = ListNode(1)
        
        return head.next
        