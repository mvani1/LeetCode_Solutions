# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        visited = set()
        curr = head
        
        while curr:
            if curr not in visited:
                visited.add(curr)
            else:
                return True
            curr=curr.next
        return False