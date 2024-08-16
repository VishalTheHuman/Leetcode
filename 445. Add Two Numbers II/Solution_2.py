# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]: 
        s1,s2 = [],[]
        while l1 or l2:
            s1.append(l1.val) if l1 else None
            s2.append(l2.val)  if l2 else None
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        head = None
        carry = 0

        while s1 or s2 or carry:
            a = s1.pop() if s1 else 0
            b = s2.pop() if s2 else 0
            val = a + b + carry
            if val>9:
                val = val%10
                carry = 1
            else:
                carry = 0
            head = ListNode(val,head)

        return head