class Solution:
    def dfs(self,i,j,visited,grid,n,m):
        if (i<0 or j<0 or i>=n or j>=m or visited[i][j] or grid[i][j]!="1" ):
            return
        visited[i][j]= True

        self.dfs(i-1,j,visited,grid,n,m)
        self.dfs(i+1,j,visited,grid,n,m)
        self.dfs(i,j-1,visited,grid,n,m)
        self.dfs(i,j+1,visited,grid,n,m)

    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        n = len(grid)
        m = len(grid[0])
        visited = [[False]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j]=="1" and not visited[i][j]:
                    self.dfs(i,j,visited,grid,n,m)
                    islands+=1
        return islands