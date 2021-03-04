# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        output = ""
        while head:
            output+=str(head.val)
            head = head.next
        if len(output)==1:return output[0]
        count = 0
        final = 0
        
        for i in output[::-1]:
            if i == "1":
                final+=(2**count)
            count+=1
        return final
        