# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        self.minn = []
        def t(root):
            if not root:return
            self.minn.append(root.val)
            t(root.left)
            t(root.right)
        t(root)
        self.minn.sort()
        res = [j - i for i, j in zip(self.minn[: -1], self.minn[1 :])]
        return min(res)