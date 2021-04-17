# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = l1
        b = l2
        num1 = ""
        num2 = ""
        while a:
            num1+=str(a.val)
            a=a.next
        while b:
            num2+=str(b.val)
            b=b.next
        rvs = str(int(num1[::-1])+int(num2[::-1]))[::-1]
        new_node = ListNode(int(rvs[0]))
        head = new_node
        for i in rvs:
            node = ListNode(int(i))
            head.next = node
            head= head.next
        return new_node.next
            