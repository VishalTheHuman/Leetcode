# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        itr = head
        count = 0
        while itr:
            count+=1
            itr = itr.next
        if count - n == 0:
            return head.next
        itr = head
        count = count - n
        i = 0
        while itr:
            i+=1
            if i==count:
                itr.next = itr.next.next
                break
            itr = itr.next
        return head