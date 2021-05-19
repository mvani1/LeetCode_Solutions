# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        '''
        Brute : 
            Method 1 (Naïve): 
            This method doesn’t require the tree to be a BST. Following are the steps. 
            1. Traverse node by node(Inorder, preorder, etc.) 
            2. For each node find all the nodes greater than that of the current node, 
                sum the values. Store all these sums. 
            3. Replace each node value with their corresponding sum by traversing in the same order as in Step 1. 
            This takes O(n^2) Time Complexity.
        
        Optimal :
            By leveraging the fact that the tree is a BST, we can find an O(n) solution. 
            The idea is to traverse BST in reverse inorder. 
            Reverse inorder traversal of a BST gives us keys in decreasing order. 
            Before visiting a node, we visit all greater nodes of that node. 
            While traversing we keep track of the sum of keys which is the 
            sum of all the keys greater than the key of the current node. 
            
        '''
        def traverse(root):
            if not root:return
            traverse(root.right)
            self.total += root.val
            root.val = self.total
            traverse(root.left)
            
        self.total = 0
        traverse(root)
        return root