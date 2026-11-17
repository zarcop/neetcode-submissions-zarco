class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        """
        placing n queens in an n * n chessboard so that queens can not attack each other
        in chess a queen can attack each other vertically horizontally an diagonally.
        given an integ
        return all the n distincs solutions to this problem
        """
        result =  []


        board = [['.'] * n for _ in range(n)]

        used_rows = set()
        used_diag = set()
        used_anti = set()


        def backtrack(col):
            if col == n:
                formatted_board = ["".join(row) for row in board]
                result.append(formatted_board)
            for row in range(n):
                if (row in used_rows or (row + col) in used_diag
                or (row - col) in used_anti):
                    continue
                board[row][col] = "Q"
                used_rows.add(row)
                used_diag.add(row + col)
                used_anti.add(row - col)
                backtrack(col + 1)
                board[row][col] = "."
                used_rows.remove(row)
                used_diag.remove(row + col)
                used_anti.remove(row - col)
        

        backtrack(0)

        return result
       
            
            
            
    
        

            

                


    


        







        