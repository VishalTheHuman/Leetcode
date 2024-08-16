# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        itr = head
        if itr.val > 4:
            head = ListNode(1,itr)
        while itr:
            itr.val = (itr.val*2)%10 + (1 if itr.next and itr.next.val > 4 else 0)
            itr = itr.next
        return head