# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        list_search = []
        def search_dfs(root,types):
            nonlocal list_search
            stack = [root]
            while stack:
                curr = stack.pop()
                if types == 1:
                    list_search.append(target-curr.val)
                else:
                    if curr.val in list_search:
                        return True
                if curr.left:
                    stack.append(curr.left)
                if curr.right:
                    stack.append(curr.right)
        search_dfs(root1,1)
        return search_dfs(root2,2)
        # print(list_search)
        