class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False]*n

        def dfs(city):
            visited[city] = True
        
            for neighbour in range(n):
                if isConnected[city][neighbour] == 1 and not visited[neighbour]:
                    dfs(neighbour)
        province = 0
        for city in range(n):
            if not visited[city]:
                province += 1
                dfs(city)
        return province