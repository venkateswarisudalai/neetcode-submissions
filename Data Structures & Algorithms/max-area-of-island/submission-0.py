class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        column = len(grid[0])
        row = len(grid)
        max_count=0
        def dfs(i,j):
            if i<0 or j<0 or i>=row or j>=column:
                return 0

            if grid[i][j] == 0:
                return 0

            grid[i][j] = 0
            
            return 1 + (dfs(i-1, j) + dfs(i+1, j) + dfs(i, j-1) + dfs(i, j+1))    
            
       





        for i in range(row):
            for j in range(column):
                if grid[i][j] == 1:
                    
                    area = dfs(i,j)
                    max_count = max(area,max_count)
                    

        return max_count
        