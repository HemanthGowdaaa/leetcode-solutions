class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        parent = list(range(len(edges)+1))

        def search_top(v):
            if parent[v]!=v:
                parent[v] = search_top(parent[v])
            return parent[v]

        for edge in edges:
            v1 = search_top(edge[0])
            v2 = search_top(edge[1])

            if v1 == v2:
                return edge
            parent[v1]=v2






        # graph = {}

        # def dfs(node,target,visited):
        #     if node == target:
        #         return True
        #     visited.add(node)
        #     for neighbour in graph.get(node,[]):
        #         if neighbour not in visited:
        #             if dfs(neighbour,target,visited):
        #                 return True
        #     return False


        # for u,v in edges:
        #     visited = set()

        #     if dfs(u,v,visited):
        #         return [u,v]

        #     graph.setdefault(u,[]).append(v)
        #     graph.setdefault(v,[]).append(u)

        # return []