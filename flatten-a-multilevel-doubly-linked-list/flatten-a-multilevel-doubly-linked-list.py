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
        curr = head
        while curr:
            if curr.child:
                temp = curr.next
                new_next = curr.child
                curr.next = curr.child
                curr.child.prev = curr
                curr.child = None
                while new_next.next:
                    new_next = new_next.next
                new_next.next = temp
                if temp:
                    temp.prev = new_next
            curr = curr.next
        return head