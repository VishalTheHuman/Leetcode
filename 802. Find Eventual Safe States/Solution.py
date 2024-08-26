class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        V = len(graph)
        terminal = [False] * V
        visited = [False] * V
        
        def dfs(node): 
            if visited[node] or terminal[node]: 
                return terminal[node]

            visited[node] = True
        
            for x in graph[node]: 
                if not dfs(x): 
                    return False
            
            terminal[node] = True

            return True
                    

        for i in range(V): 
            if not visited[i]: 
                dfs(i)
        
        return [idx for idx in range(V) if terminal[idx]]
