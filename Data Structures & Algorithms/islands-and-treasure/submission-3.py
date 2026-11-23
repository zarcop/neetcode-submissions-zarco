from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        INF = 2147483647
        queue = deque()

        # Push ALL treasures into the queue first
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 0:
                    queue.append((row, col, 0))

        while queue:
            r, c, distance = queue.popleft()
            next_dist = distance + 1

            # Only visit unvisited land cells (INF), and mark BEFORE pushing
            if r > 0 and grid[r - 1][c] == INF:
                grid[r - 1][c] = next_dist
                queue.append((r - 1, c, next_dist))
            if r < m - 1 and grid[r + 1][c] == INF:
                grid[r + 1][c] = next_dist
                queue.append((r + 1, c, next_dist))
            if c > 0 and grid[r][c - 1] == INF:
                grid[r][c - 1] = next_dist
                queue.append((r, c - 1, next_dist))
            if c < n - 1 and grid[r][c + 1] == INF:
                grid[r][c + 1] = next_dist
                queue.append((r, c + 1, next_dist))
        