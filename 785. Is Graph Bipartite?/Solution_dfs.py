class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        V = len(graph)
        colors = [-1] * V
        result = True

        def dfs(node, color=0):
            nonlocal result
            if colors[node] != -1:
                if colors[node] != color:
                    result = False
                return
            colors[node] = color
            for x in graph[node]:
                if result:
                    dfs(x, (color + 1) % 2)

        for i in range(V):
            if result and colors[i] == -1:
                dfs(i)
        
        return result
