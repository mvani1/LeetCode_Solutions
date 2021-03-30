# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.res= []
        def bfs(root):
            if root is None:
                return
            if root.left and root.left.left is None and root.left.right is None:
                self.res.append(root.left.val)
            bfs(root.left)
            bfs(root.right)
        bfs(root)
        print(self.res)
        return sum(self.res)