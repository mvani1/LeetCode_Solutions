# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        start = ord('a')
        out = []
        self.c = 1
        def traverse(root,path):
            nonlocal out
            if not root:
                return
            path+=chr(root.val+start)
            traverse(root.left,path)
            traverse(root.right,path)
            if not root.left and not root.right:
                out.append(path[::-1])
                
            
        traverse(root,"")
        return min(out)
        