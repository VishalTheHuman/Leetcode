﻿# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        result = []
        stk = []
        i = 0
        while head:
            result.append(0)
            while stk and stk[-1][0] < head.val:
                result[stk.pop()[1]] = head.val
            stk.append((head.val, i))
            i += 1
            head = head.next
        return result
