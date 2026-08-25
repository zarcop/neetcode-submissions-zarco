class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) - 1
        n = len(matrix[0]) - 1
        left_m = 0
        right_m = m
        while left_m <= right_m:
            midpoint_m = (left_m + right_m) // 2
            if matrix[midpoint_m][0] <= target <= matrix[midpoint_m][n]:
                left = 0
                right = n
                while left <= right:
                    midpoint = (right + left) // 2
                    if matrix[midpoint_m][midpoint] == target:
                        return True
                    elif matrix[midpoint_m][midpoint] < target:
                        left = midpoint + 1
                    else:
                        right = midpoint - 1
                return False
            elif target < matrix[midpoint_m][0]:
                right_m = midpoint_m - 1
            else:
                left_m = midpoint_m + 1
        return False


        
        