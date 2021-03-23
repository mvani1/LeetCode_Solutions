# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None: return head
        dummy = ListNode('#')
        first = head
        
        
        while first is not None:
            second = first.next
            first.next = dummy
            dummy = first
            first = second
        result = dummy
        
        while dummy.next.val != '#':
            dummy = dummy.next
        dummy.next = None
            
        return result
            
            