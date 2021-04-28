class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        WORD_KEY = '$'
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                # retrieve the next node; If not found, create a empty node.
                node = node.setdefault(letter, {})
            # mark the existence of a word in trie node
            node[WORD_KEY] = word
        rowNum = len(board)
        colNum = len(board[0])
        
        matchedWords = []
        
        def backtracking(row,col,trie):
            if row>=rowNum or col>=colNum or row<0 or col<0 :
                return
            letter = board[row][col]
            currNode = trie[letter]
            word_match = currNode.pop(WORD_KEY, False)
            if word_match:
                matchedWords.append(word_match)
            board[row][col] = '#'

            for (rowOffset, colOffset) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                newRow, newCol = row + rowOffset, col + colOffset     
                if newRow < 0 or newRow >= rowNum or newCol < 0 or newCol >= colNum:
                    continue
                if not board[newRow][newCol] in currNode:
                    continue
                backtracking(newRow, newCol, currNode)
        
            board[row][col] = letter
        
            # Optimization: incrementally remove the matched leaf node in Trie.
            # if not currNode:
            #     parent.pop(letter)
        
        for row in range(rowNum):
            for col in range(colNum):
                if board[row][col] in trie:
                    backtracking(row, col, trie)
        return matchedWords
        
        