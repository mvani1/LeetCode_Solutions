# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def traverse(root):
            if not root:return 0
            count = 1 if root == p or root == q else 0
            count += traverse(root.left)
            if (count < 2):
                count += traverse(root.right)
            if (count == 2):
                self.ans = root
                return 3
            return count
        
        traverse(root)
        return self.ans
        
