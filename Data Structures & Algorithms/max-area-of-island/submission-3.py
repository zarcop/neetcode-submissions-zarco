from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        m, n = len(grid), len(grid[0])
        max_size = 0

        def dfs(row: int, col: int) -> int:
            if (
                not (0 <= row < m and 0 <= col < n)
                or grid[row][col] == 0
                or (row, col) in visited
            ):
                return 0

            visited.add((row, col))
            return (
                1
                + dfs(row + 1, col)
                + dfs(row - 1, col)
                + dfs(row, col + 1)
                + dfs(row, col - 1)
            )

        for row in range(m):
            for col in range(n):
                if (row, col) not in visited and grid[row][col] == 1:
                    max_size = max(max_size, dfs(row, col))

        return max_size
        


            
            
            


        


    
        