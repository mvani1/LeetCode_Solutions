# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        # pre = root -> left -> right
        # post = left -> right -> root
        '''
                1
            (452) (673)
        
        '''
        pre_index, pre_end = 0, len(pre)-1
        post_index,post_end = 0, len(post)-1
        return self.construct(pre,pre_index,pre_end,post,post_index,post_end)
        
    def construct(self,pre,preStart,preEnd,post,postStart,postEnd):
        if preStart > preEnd: return None
        
        root = TreeNode(pre[preStart])
        
        if preStart == preEnd :return root
        
        postIndex = postStart
        
        while pre[preStart+1]!=post[postIndex] : postIndex+=1
            
        preLen = postIndex - postStart + 1
        root.left = self.construct(pre,preStart+1,preStart+preLen,post,postStart,postIndex)
        root.right = self.construct(pre,preStart+preLen+1,preEnd,post,postIndex+1,postEnd-1)
        
        return root
        
        