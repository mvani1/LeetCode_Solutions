# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if not root.left and not root.right:
            return root.val
        c = 0
        q = deque([(root,c)])
        left_most = 0
        while q:
            size = len(q)
            c +=1 
            prev = 0
            for i in range(size):
                node,_ = q.popleft()
                if node.left:
                    q.append((node.left,c))
                if node.right:
                    q.append((node.right,c))
                if prev<_:
                    left_most = node.val
                    prev = _
        return left_most