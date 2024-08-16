# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1,s2 = [],[]
        while l1 and l2:
            s1.append(l1.val)
            s2.append(l2.val)
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        
        head = None
        carry = 0

        while s1 and s2:
            val = s1.pop() + s2.pop() + carry
            if val>9:
                val = val%10
                carry = 1
            else:
                carry = 0
            head = ListNode(val,head)

        while s1:
            val = s1.pop()+carry
            if val>9:
                val = val%10
                carry = 1
            else:
                carry = 0
            head = ListNode(val,head)
        
        while s2:
            val = s2.pop()+carry
            if val>9:
                val = val%10
                carry = 1
            else:
                carry = 0
            head = ListNode(val,head)
        
        if carry:
            head = ListNode(carry,head)

        return head