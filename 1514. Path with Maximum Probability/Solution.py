class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:

        graph = defaultdict(list)
        for (u, v), weight in zip(edges, succProb):
            graph[u].append((v, weight))
            graph[v].append((u, weight))
        
        visited = [False] * n
        heap = [(-1, start_node)]

        while heap:
            p, node = heapq.heappop(heap)
            if node == end_node: 
                return -p

            visited[node] = True
            for x, nextProb in graph[node]:
                if not visited[x]: 
                    heapq.heappush(heap, (p*nextProb, x))
        
        return 0
