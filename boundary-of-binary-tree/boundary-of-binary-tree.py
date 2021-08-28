# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        def dfs_left(root):
            if not root or not root.left and not root.right:
                return
            res.append(root.val)
            if root.left:
                dfs_left(root.left)
            else:
                dfs_left(root.right)
        def dfs_right(root):
            if not root or not root.left and not root.right:
                return
            if root.right:
                dfs_right(root.right)
            else:
                dfs_right(root.left)
            res.append(root.val)
                

        def leaves(node):
            if not node:
                return
            leaves(node.left)
            if node != root and not node.left and not node.right:
                res.append(node.val)
            leaves(node.right)

        res = [root.val]
        dfs_left(root.left)
        leaves(root)
        dfs_right(root.right)
        return(res)