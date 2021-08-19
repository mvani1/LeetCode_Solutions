"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def __init__(self):
        self.seen = {}
        
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:return node
        if node in self.seen:
            return self.seen[node]
        new_node = Node(node.val)
        self.seen[node] = new_node
        for neigh in node.neighbors:
            next_new_node = self.cloneGraph(neigh)
            new_node.neighbors.append(next_new_node)
        return new_node