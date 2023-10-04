# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        i = 1
        start = None
        l = list1
        while l:
            if i==a:
                start = l
            if i==b:
                l = l.next
                break
            i+=1
            l = l.next
        start.next = list2
        while start.next:
            start = start.next
        start.next = l.next
        return list1