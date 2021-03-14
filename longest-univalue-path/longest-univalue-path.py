# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if root is None:return 0
        self.count = 0
        self.ans = 0 
        def f(root):
            if root is None:return 0
            left = f(root.left)
            right = f(root.right)
            l=r=0
            if root.left and root.left.val==root.val:
                l=left+1
            if root.right and root.right.val==root.val:
                r=right+1
            self.ans = max(self.ans,l+r)
            return max(l,r)
        f(root)
        return self.ans
                