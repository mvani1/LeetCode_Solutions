# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def dfs(root):
            if not root:
                return
            if low <= root.val <= high:
                self.result += root.val
            dfs(root.left)
            dfs(root.right)
        self.result = 0   
        dfs(root)
        return self.result