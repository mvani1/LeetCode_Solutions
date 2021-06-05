"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""
class NodeCopy:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
        
class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root:return 
        def fill(node):
            if not node:
                return 
            hash[node] = NodeCopy(node.val)
            for child in node.children:
                hash[node].children.append(fill(child))
            return hash[node]
        hash = {}
        fill(root)
        return(hash[root])