class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inDegree = [0]*numCourses
        graph = defaultdict(list)

        for u,v in prerequisites: 
            graph[u].append(v)
            inDegree[v] += 1
        
        q = deque([])

        for idx in range(len(inDegree)): 
            if inDegree[idx] == 0: 
                q.append(idx)

        result = []

        while q: 
            for _ in range(len(q)):
                node = q.popleft()
                result.append(node)
                for x in graph[node]:
                    inDegree[x] -= 1
                    if inDegree[x] == 0: 
                        q.append(x)
    
        return not any(inDegree)
