class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        nrows = len(board)
        ncols = len(board[0])

        def backtrack(row, col, word_i):
            if word_i == len(word):
                return True
            
            if not (0 <= row < nrows and 0 <= col < ncols) or board[row][col] != word[word_i]:
                return False
            temp = board[row][col]
            board[row][col] = "#"
            found  =  (backtrack(row + 1, col, word_i + 1) or
                     backtrack(row - 1, col, word_i + 1) or
                     backtrack(row, col + 1, word_i + 1) or
                     backtrack(row, col - 1, word_i + 1))
            board[row][col] = temp
            return found
        
        for r in range(nrows):
            for c in range(ncols):
                if backtrack(r, c, 0):
                    return True
        

        return False


            
            
        


        