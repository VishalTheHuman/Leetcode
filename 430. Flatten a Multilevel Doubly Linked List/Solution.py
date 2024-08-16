"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: 
            return head
        itr = head
        stk = []
        while itr:
            if itr.child:
                if itr.next:
                    stk.append(itr.next)
                itr.next = itr.child
                itr.child.prev = itr
                itr.child = None
            prev = itr
            itr = itr.next
        while stk:
            node = stk.pop()
            prev.next = node
            node.prev = prev
            while node.next:
                prev = node
                node = node.next
            prev = node
        return head