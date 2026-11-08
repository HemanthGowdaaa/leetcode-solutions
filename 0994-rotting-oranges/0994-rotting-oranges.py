from collections import deque
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        m,n = len(grid),len(grid[0])
        q = deque()
        time, fresh = 0,0
        directions = [[1,0],[-1,0],[0,-1],[0,1]]
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    fresh+=1
                if grid[r][c] == 2:
                    q.append([r,c])

        while q and fresh > 0:
            for _ in range(len(q)):
                r,c = q.popleft()
                for dr,dc in directions:
                    row,col = dr+r , dc+c
                    if row >= m or row < 0 or col >= n or col < 0 or grid[row][col]!=1:
                        continue
                    grid[row][col]=2
                    fresh-=1
                    q.append([row,col])
            time+=1
        return time if fresh == 0 else -1