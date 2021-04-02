# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        level = [root]
        next_level = []    #(left/right,parent_val)
        flag = 0
        while level:
            size = len(level)
            bfs = []
            
            for i in range(size):
                node = level.pop(0)
                if node.left:
                    level.append(node.left)
                    next_level.append((node.left.val,node.val))
                if node.right:
                    level.append(node.right)
                    next_level.append((node.right.val,node.val))
                bfs.append(node.val)
                if x in bfs and y in bfs:
                    flag = 1
        # print(next_level,fag)
        x_par,y_par = 0,0
        if flag:
            for val in next_level:
                if x == val[0]:
                    x_par = val[1]
                if y == val[0]:
                    y_par = val[1]
                if x_par and y_par:
                    if x_par!=y_par:
                        return True
        else:
            return False
            
            