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
    def flatten(self, head: 'Node') -> 'Node':
        ref = head
        child_stack = []
        nxt_stack = []       
        while ref:

            if ref.child:
                child_stack.append(ref.child)
                if ref.next is not None:
                    nxt_stack.append(ref.next)
            
            if child_stack:
                temp = child_stack.pop(0)
                ref.child = None
                temp.prev = ref
                ref.next = temp
                
            if ref.next is None:
                if nxt_stack:
                    temp1 = nxt_stack.pop()
                    temp1.prev = ref
                    ref.next = temp1
                    # ref=ref.next   
            ref = ref.next
            
        return head
                
            
            