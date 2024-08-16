# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stk = []
        while head:
            stk.append(head.val)
            head = head.next
        carry = 0
        head = None
        while stk:
            val = stk.pop()*2  + carry
            carry = val // 10
            val = val % 10
            
            head = ListNode(val,head)
        if carry:
            head = ListNode(1,head)
        return head