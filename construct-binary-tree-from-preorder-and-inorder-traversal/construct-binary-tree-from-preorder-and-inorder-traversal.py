# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        '''
        pre [3,9,20,15,7]
        in  [9,3,15,20,7]
        '''
        if inorder:
            root = TreeNode(preorder.pop(0))
            idx = inorder.index(root.val)
            root.left = self.buildTree(preorder,inorder[:idx:])
            root.right = self.buildTree(preorder,inorder[idx+1::])
            # print(root)
            return root
        else:return
            