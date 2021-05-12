# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None
        def traverse(root):
            if not root:return 0
            if p == root or q == root:
                count = 1
            else:
                count = 0
            count += traverse(root.left) + traverse(root.right)
            if count == 2:
                self.ans = root
                return 3
            return count
        traverse(root)
        return self.ans