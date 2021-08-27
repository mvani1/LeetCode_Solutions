# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        queue = deque([])
        max_zig_zag = 0

        if root.left:
            queue.append((root.left,"l",1))
        if root.right:
            queue.append((root.right,"r",1))
        
        
        while queue:
            node, from_, zig_zag_step = queue.popleft()
            max_zig_zag = max(max_zig_zag, zig_zag_step)
            
            if node.left:
                if from_ == 'l':
                    queue.append((node.left,'l',1))
                if from_ == 'r':
                    queue.append((node.left,'l', zig_zag_step + 1))
                    
            if node.right:
                if from_ == 'r':
                    queue.append((node.right,'r',1))
                if from_ == 'l':
                    queue.append((node.right,'r', zig_zag_step + 1))
        return max_zig_zag
                    
            