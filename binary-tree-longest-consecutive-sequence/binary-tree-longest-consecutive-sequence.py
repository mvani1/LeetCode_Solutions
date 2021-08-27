# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        queue = deque([(root,1)])
        max_seq = 0
        while queue:
            node, seq = queue.popleft()
            max_seq = max(max_seq,seq)
            if node.left:
                if node.val+1 == node.left.val:
                    queue.append((node.left,seq+1))
                else:
                    queue.append((node.left,1))
            if node.right:
                if node.val+1 == node.right.val:
                    queue.append((node.right,seq+1))
                else:
                    queue.append((node.right,1))
            
        return max_seq