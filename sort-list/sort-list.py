# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None: return head
        curr = head
        slow = head
        fast = head
        while fast and fast.next:
            curr = slow
            slow = slow.next
            fast = fast.next.next
        curr.next = None
        l1 = self.sortList(head)
        l2 = self.sortList(slow)
        return self.mergeSort(l1,l2)
        
    def mergeSort(self,l1,l2):
        if l1 is None: return l2
        elif l2 is None: return l1
        elif l1.val < l2.val:
            l1.next = self.mergeSort(l1.next,l2)
            return l1
        else:
            l2.next = self.mergeSort(l1,l2.next)
            return l2