# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Node') -> 'NodeCopy':
        curr = dummy = Node()
        if root is None:
            return None
        l1 = root
        h = {}
        def traverse(root):
            if root is None:return 
            h[root] = NodeCopy(root.val)
            traverse(root.left)
            traverse(root.right)
        traverse(root)
        def traver(root):
            if root is None:return
            if root.left:
                h[root].left = h[root.left]
            if root.right:
                h[root].right = h[root.right]
            if root.random:
                h[root].random = h[root.random]
            traver(root.left)
            traver(root.right)
        traver(l1)   
            
                
#         level = [root]
#         while level: 
#             next_leve =[]
#             for node in level:
#                 if node.left:
#                     h[node].left = h[node.left]
#                     next_leve.append(node.left)
#                 if node.right:
#                     h[node].right = h[node.right]
#                     next_leve.append(node.right)
#                 if node.random:
#                     h[node].random = h[node.random]
#             level = next_leve
        return h[root]
                