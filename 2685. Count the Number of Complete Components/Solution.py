class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u,v in edges: 
            graph[u].append(v)
            graph[v].append(u)
        
        count = 0 
        visited = [False] * n 

        def dfs(node, known): 
            visited[node] = True
            possible = True
            for x in graph[node]:
                if visited[x]: 
                    continue
                if x not in known:
                    possible = False
                
                if not dfs(x, known): 
                    possible = False
                
            if len(graph[node]) != N:
                possible = False
            return possible
           
        for i in range(n): 
            if not visited[i]: 
                known = set(graph[i]+[i])
                N = len(graph[i])
                count += dfs(i, known)
        return count
