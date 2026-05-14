class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        visited=set()
        def dfs(row,col):
            if row<0 or row>=m or col>=n or col<0 or grid[row][col]==0:
                return 1
            if (row,col) in visited:
                return 0
            visited.add((row,col))
            perimeter=0
            perimeter+=dfs(row,col+1)
            perimeter+=dfs(row+1,col)
            perimeter+=dfs(row,col-1)
            perimeter+=dfs(row-1,col)
            return perimeter



        for r in range(m):
            for c in range(n):
                if grid[r][c]==1:
                    return dfs(r,c)
        