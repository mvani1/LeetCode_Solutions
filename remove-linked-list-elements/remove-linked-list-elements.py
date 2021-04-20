# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head: return head
        sentinel = ListNode(-22,head)
        curr = head
        prev = sentinel
        while curr:
            if curr.val == val:
                temp = curr.next
                curr = prev
                curr.next = temp
            prev = curr
            curr = curr.next
        return sentinel.next
            