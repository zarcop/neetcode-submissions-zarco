class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:


        num = 0
        m = len(grid)
        n = len(grid[0])


        def dfs_and_mark(row, col) -> None:
            if not(0 <= row < m and 0 <= col < n) or grid[row][col] == '0':
                return
            grid[row][col] = "0"
            dfs_and_mark(row + 1, col)
            dfs_and_mark(row-1, col)
            dfs_and_mark(row,col+1)
            dfs_and_mark(row, col - 1)

        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    dfs_and_mark(r,c)
                    num += 1
        
        return num

                


        

      



    