# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        i = 1
        nodeA = nodeB = list1
        while i < b+1:
            if i < a:
                nodeA = nodeA.next
            i+=1
            nodeB = nodeB.next
        nodeA.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = nodeB.next
        return list1