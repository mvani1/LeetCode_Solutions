# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return None
        left,right = head,head
        stop = False
        def recur(right,m,n):
            nonlocal left,stop
            if n == 1:
                return 
            right = right.next
            if m > 1:
                left = left.next
                
            recur(right,m-1,n-1)
            if left == right or right.next == left:
                stop = True
            if not stop : 
                left.val,right.val = right.val,left.val
                left = left.next
            
            
        recur(right,m,n)
        return head
        
        
        
        
        
#         counter = 0
#         while curr:
#             if curr.next and counter+1 == left:
#                 prev = curr
#             counter +=1
#             if counter == left:
#                 leftP = curr
#             if counter == right:
#                 rightP = curr
            
#             curr = curr.next
        
#         prev.next = None
        
#         if rightP.next:
#             remaining = rightP.next
        
#         curr = leftP
#         newPrev = remaining
#         rightP.next = None
#         while curr:
#             temp = curr.next
#             curr.next = newPrev
#             newPrev = curr
#             curr = temp
            
#         prev.next = newPrev
#         return head
        
            