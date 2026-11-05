class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        for pre, crs in prerequisites:
            preMap[pre].append(crs)
        visited = set()

        def dfs(crs):
            if crs in visited:
                return False
            if preMap[crs] == []:
                return True
            visited.add(crs)
            for cr in preMap[crs]:
                if not dfs(cr):
                    return False
            visited.remove(crs)
            preMap[crs] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
            
        