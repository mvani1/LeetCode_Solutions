class Solution:
    
    def countBattleships(self, board: List[List[str]]) -> int:
        # print(board)
        c = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=='X':
                    if ((i==0 or board[i-1][j] == '.') or (i==len(board[0]) and board[i+1][j]==".")) and ((j==0 or board[i][j-1] == '.') or (j==len(board[0]) and board[i][j+1]==".")):
                        c+=1
        return c