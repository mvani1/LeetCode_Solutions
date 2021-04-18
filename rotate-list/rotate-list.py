# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        start = prev = curr = head
        length = 0
        tail = prev
        while prev:
            length+=1
            tail = prev
            prev=prev.next
        if length == 0 or k ==0 or k%length == 0 :
            return head
        
        k = k%length
        
        index = length - k
        local_counter = 1
        while curr:
            if index == local_counter:
                start = curr.next
                curr.next = None
            local_counter+=1
            curr = curr.next
        tail.next = head
        return start
            
        
        
        