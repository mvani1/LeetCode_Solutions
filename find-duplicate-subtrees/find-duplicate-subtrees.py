# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        def traverse(root):
            if not root:return 'null'
            key = '%s,%s,%s' % (str(root.val),traverse(root.left),traverse(root.right))
            # print(key)
            if key in dups:
                liss.add(key)
            dups[key] = root
            return key
        dups = {}
        liss = set()
        traverse(root)

        return [dups[struct] for struct in liss]