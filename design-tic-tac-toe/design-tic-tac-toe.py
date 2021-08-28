class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.rows = [0 for i in range(n)]
        self.cols = [0 for i in range(n)]
        self.n = n
        self.diagonal = 0
        self.antidiagonal = 0
    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        current_player = 1 if player == 1 else -1
        self.rows[row] += current_player
        self.cols[col] += current_player
        if row == col:
            self.diagonal += current_player
        if col == (self.n - row - 1):
            self.antidiagonal += current_player
        if abs(self.rows[row])==self.n or abs(self.cols[col])==self.n \
            or abs(self.diagonal)==self.n or abs(self.antidiagonal)==self.n:
            return player
        return 0
# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)