class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        rows, cols = len(matrix), len(matrix[0])

        # Part 1: Binary search to find the correct row
        bottom_row, top_row = 0, rows - 1
        actual_row = -1

        while bottom_row <= top_row:
            # FIX 1: Correct midpoint calculation
            mid_row = bottom_row + (top_row - bottom_row) // 2
            
            # Check if the target is within the bounds of this mid_row
            # FIX 2: Use cols-1 for the last column index
            if matrix[mid_row][0] <= target <= matrix[mid_row][cols - 1]:
                actual_row = mid_row
                break
            elif target > matrix[mid_row][cols - 1]:
                bottom_row = mid_row + 1
            else: # target < matrix[mid_row][0]
                top_row = mid_row - 1

        if actual_row == -1:
            return False

        # Part 2: Binary search within the identified row
        bottom, top = 0, cols - 1 # FIX 4: Correct top boundary
        while bottom <= top:
            # FIX 1: Correct midpoint calculation
            mid = bottom + (top - bottom) // 2
            
            if target == matrix[actual_row][mid]:
                return True
            # FIX 3: Update bottom and top pointers, not mid
            elif target > matrix[actual_row][mid]:
                bottom = mid + 1
            else:
                top = mid - 1
                
        return False
        



        