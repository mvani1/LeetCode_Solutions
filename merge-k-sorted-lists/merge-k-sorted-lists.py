# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        while len(lists)!=1:
            lists.append(self.merge2lists(lists.pop(),lists.pop()))
        
        return lists[0]
            
    def merge2lists(self,l1,l2):
        # if l1 == [] and l2.val != []:
        #     return l2
        # elif l2.val == [] and l1.val!=[]:
        #     return l1
        if not l1:
            return l2
        elif not l2:
            return l1
        elif l1.val < l2.val:
            l1.next = self.merge2lists(l1.next,l2)
            return l1
        else:
            l2.next = self.merge2lists(l1,l2.next)
            return l2