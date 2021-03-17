# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a,b=l1,l2
        temp,temp2 = [],[]
        while a:
            temp.append(str(a.val))
            a = a.next
        while b:
            temp2.append(str(b.val))
            b = b.next
        sums = str(int("".join(temp))+int("".join(temp2)))
        result = ListNode(int(sums[0]))
        out = result
        for i in range(1,len(sums)):
            out.next = ListNode(sums[i])
            out = out.next

        return result
            