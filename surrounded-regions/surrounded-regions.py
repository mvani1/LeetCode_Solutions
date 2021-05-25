class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.seen = set()
        
        def validity(x,y):
            if x<0 or y<0 or x>=R or y>=C or board[x][y]!='O' or (x,y) in self.seen:
                return False
            self.seen.add((x,y))
            validity(x,y-1)
            validity(x,y+1)
            validity(x-1,y)
            validity(x+1,y)
        R = len(board)
        C = len(board[0])
        def checker():    
            for i in range(C):
                if board[0][i] == 'O':
                    validity(0,i)

            for i in range(R):
                if board[i][0] == 'O':
                    validity(i,0)
            for i in range(C):
                if board[R-1][i] == 'O':
                    validity(R-1,i)
            for i in range(R):
                if board[i][C-1] == 'O':
                    validity(i,C-1)
        checker()
        
        for i in range(R):
            for j in range(C):
                if board[i][j] == 'O' and (i,j) not in self.seen:
                    board[i][j] = 'X'
        
        
        

            
                