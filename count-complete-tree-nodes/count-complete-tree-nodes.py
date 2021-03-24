# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root is None: return 0
        self.count = 1
        def dfs(root):
            if root is None:
                return
            if root.left:
                self.count+=1
                dfs(root.left)
            elif root.left is None and root.right:
                self.count-=1
            if root.right:
                self.count+=1
                dfs(root.right)
            # else:
                # self.count-=1
        dfs(root)
        return self.count