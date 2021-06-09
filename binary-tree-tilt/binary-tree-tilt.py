# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        sums = 0
        def tilt(node):
            nonlocal sums
            if not node:return 0
            
            left = tilt(node.left)
            right = tilt(node.right)
            sums += abs(left-right)
            return node.val +left + right
            
        tilt(root)
        return sums