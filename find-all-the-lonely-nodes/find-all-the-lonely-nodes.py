# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        if not root:return
        def t(node):
            if not node:return
            if node.left and not node.right:
                res.append(node.left.val)
            elif not node.left and node.right:
                res.append(node.right.val)
            t(node.left)
            t(node.right)
        res = []
        t(root)
        return res