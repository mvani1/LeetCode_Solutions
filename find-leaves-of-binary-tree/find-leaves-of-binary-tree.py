# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        node_list = deque()
        def maxDepth(root):
            if not root: return 0
            
            height =  max(maxDepth(root.left),maxDepth(root.right))+1
            node_list.append([root.val,height])
            return height
        
        height = maxDepth(root)
        result = [[] for _ in range(height)]
        for node,height in node_list:
            result[height-1].append(node)
        return result