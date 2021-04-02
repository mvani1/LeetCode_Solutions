"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:return root
        
        level = [root]
        while level:
            size = len(level)
            for i in range(size):
                node = level.pop(0)
                if i<size-1:
                    node.next = level[0]
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
        return root