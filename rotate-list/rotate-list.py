# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None or head.next is None or k ==0:return head
        length = 1
        second = head
        while second.next:
            second=second.next
            length +=1
        
        k = k%length
        second.next = head
        new_tail = head
        for i in range(length - k - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        
        # break the ring
        new_tail.next = None
        
        return new_head