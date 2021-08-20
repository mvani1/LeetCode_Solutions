# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head: return head
        dummy = ListNode(-21,None)
        prev = dummy
        dummy.next = head
        curr = dummy
        while curr : 
            if curr.val == val:
                temp = curr.next
                curr.next = None
                prev.next = temp
                curr = prev
            prev = curr
            curr = curr.next
        return(dummy.next)