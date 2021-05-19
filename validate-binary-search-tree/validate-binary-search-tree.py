# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def traverse(root,low=-math.inf,high=math.inf):
            if not root:return True
            if root.val<= low or root.val>=high:
                return False
            left = traverse(root.left,low,root.val)
            right = traverse(root.right,root.val,high)
            return left and right
        return traverse(root)