# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # if not lists:return []
        heap = []
        for i in lists:
            l1=i
            while l1:
                heapq.heappush(heap,l1.val)
                l1=l1.next
        curr = dummy = ListNode('#')
        while heap:
            new_node = ListNode(heapq.heappop(heap))
            curr.next = new_node
            curr = curr.next
        return (dummy.next)
        
                                