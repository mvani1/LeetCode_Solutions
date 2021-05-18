# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    Time : O(logn)
    Space: O(logn)
    '''
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:return None
        if key>root.val:
            root.right = self.deleteNode(root.right,key)
        elif key<root.val:
            root.left = self.deleteNode(root.left,key)
        else:
            if not (root.left or root.right):
                root = None
            elif root.right:
                root.val = self.sucessor(root)
                root.right = self.deleteNode(root.right,root.val)
            elif root.left:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left,root.val)

        return root
    def sucessor(self,root):
        root = root.right
        while root.left:
            root = root.left
        return root.val
    def predecessor(self,root):
        root =root.left
        while root.right:
            root=root.right
        return root.val
