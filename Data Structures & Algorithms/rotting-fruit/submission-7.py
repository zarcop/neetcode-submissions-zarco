from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])


        queue = deque([])
        min_time = 0

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 2:
                    queue.append((row,col, 0))
        


        while queue:
            row, col , time = queue.popleft()
            min_time = time
            next_time = time + 1
            if row < m - 1 and grid[row + 1][col] == 1:
                grid[row + 1][col] = 2
                queue.append((row + 1 , col, next_time))
            if row > 0 and grid[row-1][col] == 1:
                grid[row -1][col] = 2
                queue.append((row-1, col, next_time))

            if col > 0 and grid[row][col-1] == 1:
                grid[row][col-1] = 2
                queue.append((row, col-1, next_time))
            if col < n -1 and grid[row][col+1] == 1:
                grid[row][col+1] = 2
                queue.append((row, col + 1, next_time))
        
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    return -1
        

        return min_time 

                
                    




        