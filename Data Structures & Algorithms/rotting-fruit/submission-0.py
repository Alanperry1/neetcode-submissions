from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row,col=len(grid),len(grid[0])
        q=deque()
        time=0
        fresh=0
        for r in range(row):
            for c in range(col):
                if grid[r][c]==1:
                    fresh+=1
                if grid[r][c]==2:
                    q.append((r,c))

        direction=[[1,0],[-1,0],[0,1],[0,-1]]
        while fresh>0 and q:
            for i in range(len(q)):
                r,c=q.popleft()
                for a,b in direction:
                    rows,cols=r+a,c+b
                    
                    if (0<=rows<len(grid) and 0<=cols<len(grid[0]) and grid[rows][cols]==1):
                        grid[rows][cols]=2
                        q.append((rows,cols))
                        fresh-=1
            time+=1
        return time if fresh==0 else -1 