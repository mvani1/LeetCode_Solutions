class Solution:
    def create_board(self,state):
        board = []
        for row in state:
            board.append("".join(row))
        return board
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.']*n for _ in range(n)]
        self.n = n
        self.ans = []
        self.solver(board,0)
        return (self.ans)
    def solver(self,board,col):
        if col==self.n:
            self.ans.append(self.create_board(board))
            return True

        for i in range(self.n):
            if self.isSafe(board,i,col):
                board[i][col] = 'Q'
                self.solver(board,col+1)
                board[i][col] = '.'
        return False
        
    def isSafe(self,board, row, col):
        for i in range(col):
            if board[row][i] == 'Q':
                return False

        # Check upper diagonal on left side
        for i, j in zip(range(row, -1, -1), 
                        range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False

        # Check lower diagonal on left side
        for i, j in zip(range(row, self.n, 1), 
                        range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False

        return True
  
