# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        res = []
        def inorder(root):
            if not root:return
            res.append(root.val)
            inorder(root.left)
            inorder(root.right)
        inorder(root)
        return sorted(res,key= lambda x:abs(x-target))[0]
        