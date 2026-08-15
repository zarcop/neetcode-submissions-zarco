from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m = len(board)
        n = len(board[0])
        col_dict = defaultdict(list)
        box_dict = defaultdict(list)
        row_dict = defaultdict(list)
        for row in range(m):
            for col in range(n):
                value = board[row][col]
                if value == ".":
                    continue
                box_number =  (row//3) * 3 + (col//3)
                if value in col_dict[col] or value in row_dict[row] or value in box_dict[box_number]:
                    return False
                else:
                    col_dict[col].append(value)
                    row_dict[row].append(value)
                    box_dict[box_number].append(value)
        return True
                


        