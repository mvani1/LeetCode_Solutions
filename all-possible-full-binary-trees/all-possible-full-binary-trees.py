# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[TreeNode]:
        if not n&1 : return []
        if n == 1:
            return [TreeNode(0)]
        ans = []        
        for i in range(1,n,2):
            for l in self.allPossibleFBT(i):
                for r in self.allPossibleFBT(n-i-1):
                    root = TreeNode(0)
                    root.left = l
                    root.right = r
                    ans.append(root)
        return ans