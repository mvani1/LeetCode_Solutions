# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        ans = self.helper(root)
        return(ans[0])
        
    def helper(self, root):
        if not root: return True,-1
        left_tree, left_height = self.helper(root.left)
        if not left_tree: return False, 0
        right_tree, right_height = self.helper(root.right)
        if not right_tree: return False, 0
        
        return (abs(left_height - right_height) <= 1), max(left_height, right_height)+1