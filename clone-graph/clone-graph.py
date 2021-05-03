"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:return node
        cloning = {node:node.neighbors}
        queue = deque()
        cloning[node] = Node(node.val, [])
        queue.append(node)
        while queue:
            currNode = queue.popleft()
            for n in currNode.neighbors:
                if n not in cloning:
                    queue.append(n)
                    cloning[n] = Node(n.val,[])
                cloning[currNode].neighbors.append(cloning[n])
        return cloning[node]