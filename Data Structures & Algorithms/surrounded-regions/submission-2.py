from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows,cols=len(board),len(board[0])
        dir=[(1,0),(-1,0),(0,1),(0,-1)]


        def bfs():
            q=deque()
            for r in range(rows):
                for c in range(cols):
                    if ((r==0 or r==rows-1) or (c==0 or c==cols-1)) and board[r][c]=="O":
                        board[r][c]="T"
                        q.append((r,c))
            while q:
                rx,cx=q.popleft()    
                for dr,dc in dir:
                    x,y=rx+dr,cx+dc
                    if 0<=x<rows and 0<=y<cols and board[x][y]=="O":
                        board[x][y]="T"
                        q.append((x,y))

        bfs()
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="T":
                    board[r][c]="O"
                elif board[r][c]=="O":
                    board[r][c]="X"