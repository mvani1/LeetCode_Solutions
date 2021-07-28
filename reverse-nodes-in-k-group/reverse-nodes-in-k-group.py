# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        curr = head
        kTail = None
        newHead = None
        
        while curr:
            count = 0
            curr = head
            
            while count < k and curr:
                curr = curr.next
                count += 1
            
            if count == k:
                revHead = self.reverse(head,k)
                if not newHead:
                    newHead = revHead
                if kTail:
                    kTail.next = revHead
                kTail = head
                head = curr
        if kTail:
            kTail.next = head
        
        return newHead if newHead else head
    def reverse(self,head,k):
        curr = head
        prev = None
        last = None
        while k:
            temp = curr.next
            curr.next = prev
            prev = curr    
            curr = temp
            k-=1
        return prev