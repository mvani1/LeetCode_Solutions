# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        def traverse(node):
            if not node:
                return 
            if node in nodes:
                return node
            left,right =  traverse(node.left),traverse(node.right)
            if left and right:
                return node
            return left or right
        return traverse(root)