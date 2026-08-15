class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1

        while left <= right:
            mid_idx = left + (right - left) // 2
            # Convert the 1D mid-index back to 2D coordinates
            mid_val = matrix[mid_idx // cols][mid_idx % cols]

            if mid_val == target:
                return True
            elif mid_val < target:
                left = mid_idx + 1
            else:
                right = mid_idx - 1
        
        return False
        



        