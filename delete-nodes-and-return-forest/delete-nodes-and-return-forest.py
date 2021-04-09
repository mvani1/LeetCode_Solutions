# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.out = []
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        if root.val not in to_delete and root not in self.out:
            self.out.append(root)
        queue = [root]

        while queue:
            node = queue.pop(0)
            if node.val in to_delete:
                if node.left:
                    self.delNodes(node.left,to_delete)
                if node.right:
                    self.delNodes(node.right,to_delete)
                
            if node.left:
                queue.append(node.left)
                if node.left.val in to_delete:
                    node.left = None
                    
            if node.right:
                queue.append(node.right)
                if node.right.val in to_delete:
                    node.right = None
        return self.out
            
                