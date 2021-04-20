# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root :return True
        left = self.height(root.left)
        right = self.height(root.right)
        print(left,right)
        if abs(left-right)>1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        
    def height(self,root,count=0):
        if not root: return -1 
        return max (self.height(root.left,count),\
        self.height(root.right,count))+1
