class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        N, M = len(board),len(board[0])
        todo = False
        for i in range(N):
            for j in range(M-2):
                if abs(board[i][j]) == abs(board[i][j+1]) == abs(board[i][j+2])!=0:
                    board[i][j] =board[i][j+1]=board[i][j+2]= -abs(board[i][j])
                    todo = True
        for i in range(N-2):
            for j in range(M):
                if abs(board[i][j]) == abs(board[i+1][j]) == abs(board[i+2][j])!=0:
                    board[i][j] =board[i+1][j]=board[i+2][j]= -abs(board[i][j])
                    todo = True
        for c in range(M):
            wr = N-1
            for r in range(N-1,-1,-1):
                if board[r][c] >0:
                    board[wr][c] = board[r][c]
                    wr-=1
            for wr in range(wr,-1,-1):
                board[wr][c]=0
        return self.candyCrush(board) if todo else board