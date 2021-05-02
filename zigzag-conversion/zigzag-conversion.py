class Solution:
    def convert(self, s: str, numRows: int) -> str:
        matrix = [["00"] * len(s) for _ in range(numRows)]
        if numRows == 1: return s
        idx = 0
        row = 0
        col = 0
        while idx < len(s):
            
            #Go down
            while (idx < len(s) and row < numRows):
                matrix[row][col] = s[idx]
                idx += 1
                row += 1
            if idx >= len(s):
                break
            #Go reverse diagonal
            row -= 2
            col += 1
            while(idx < len(s) and row >= 0 and col < len(s)):
                matrix[row][col] = s[idx]
                idx += 1
                col += 1
                row -= 1
            row  = 1
            col -= 1
            if idx >= len(s):
                break
        result = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] != "00":
                    result.append(matrix[i][j])
        return "".join(result)