# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:return 0
        child = [root.left,root.right] 
        if not any(child):
            return 1
        min_depth = float('inf')
        for c in child:
            if c:
                min_depth = min(min_depth,self.minDepth(c))
        return min_depth + 1