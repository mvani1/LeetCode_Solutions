# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Node') -> 'NodeCopy':
        '''
        First:
            Recursively traverse the given Binary and copy key value, 
            left pointer and right pointer to clone tree. While copying, s
            tore the mapping from given tree node to clone tree node in a hashtable. 
            In the following pseudo code, ‘cloneNode’ is currently visited node of 
            clone tree and ‘treeNode’ is currently visited node of given tree. 
        TIME = O(n) 
                Each traversal costs O(n)O(n) because we check every node once. 
                We traverse the tree twice, which gives us O(n + n)= O(2n)O(n+n)=O(2n). 
        Space = O(n)
        
        '''
        hash = {}
        def traverse(root):
            if not root:return
            if root in hash:return hash[root]
            newRoot = NodeCopy(root.val)
            hash[root] = newRoot
            newRoot.left = traverse(root.left)
            newRoot.right = traverse(root.right)
            newRoot.random = traverse(root.random)
            return newRoot
        return traverse(root)
       