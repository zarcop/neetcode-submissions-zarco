from collections import deque
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        m, n = len(heights), len(heights[0])

        def bfs(starts: List[tuple]) -> set:
            visited = set(starts)
            queue = deque(starts)

            while queue:
                r, c = queue.popleft()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    # Move UPHILL (or flat) to find cells that can flow down to this ocean
                    if (
                        0 <= nr < m
                        and 0 <= nc < n
                        and (nr, nc) not in visited
                        and heights[nr][nc] >= heights[r][c]
                    ):
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            return visited

        pacific_starts = [(0, c) for c in range(n)] + [(r, 0) for r in range(m)]
        atlantic_starts = [(m - 1, c) for c in range(n)] + [(r, n - 1) for r in range(m)]

        pacific_reachable = bfs(pacific_starts)
        atlantic_reachable = bfs(atlantic_starts)

        # Cells reachable from BOTH oceans
        return [[r, c] for r, c in (pacific_reachable & atlantic_reachable)]


     
            
            

        