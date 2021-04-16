# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        queue = [(root,0,-1)]
        c = 0
        heir = [(root.val,0)]
        next_level = []
        while queue:
            size = len(queue)
            par = 0
            for i in range(size):
                curr,_,gp = queue.pop(0)
                if curr.left:
                    queue.append((curr.left,curr.val,_))
                if curr.right:
                    queue.append((curr.right,curr.val,_))
                next_level.append((curr.val,_,gp))
            par = curr.val
        # print(next_level)
        a = list(filter(lambda x:x[2]!=0 and x[2]%2==0 ,next_level))
        sums = 0
        b = list(map(lambda x:x[0],a))
        return sum(b)