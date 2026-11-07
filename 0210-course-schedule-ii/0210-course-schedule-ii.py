class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        result = []
        preMap = {i:[] for i in range(numCourses)}
        visiting = set()
        visited = set()
        for pre, crs in prerequisites:
            preMap[pre].append(crs)

        def dfs(crs):
            if crs in visited:
                return True
            if crs in visiting:
                return False
        
            

            visiting.add(crs)
            for c in preMap[crs]:
                if not dfs(c):
                    return False
            preMap[crs] = []
            visiting.remove(crs)
            visited.add(crs)
            result.append(crs)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return result