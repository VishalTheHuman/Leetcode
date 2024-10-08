class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        goodNodes = 0
        
        visited = set()
        def dfs(node):
            nonlocal goodNodes
            nodesCount = []
            visited.add(node)
            for x in graph[node]:
                if x in visited:
                    continue
                nodesCount.append(dfs(x))
            
            isGood = True
            
            for idx in range(1, len(nodesCount)):
                if nodesCount[idx-1] != nodesCount[idx]:
                    isGood = False
                    break
            if isGood:
                goodNodes += 1
                
            return sum(nodesCount) + 1
        
        dfs(0)
        
        return goodNodes
