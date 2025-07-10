class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        store = defaultdict(list)
        active = [True] * (c+1)
        belong = [i for i in range(c+1)]

        def find(x): 
            if x != belong[x]: 
                belong[x] = find(belong[x])
            return belong[x]
        
        def union(x,y): 
            belong[find(y)] = find(x)

        for src, dest in connections:
            union(src, dest)

        for i in range(1,c+1): 
            store[belong[find(i)]].append(i)

        for key in store.keys(): 
            heapq.heapify(store[key])

        results = []

        for q, node in queries: 
            if q == 1: 
                if active[node]: 
                    results.append(node)
                else:
                    answer = -1
                    while store[belong[node]]: 
                        top = heapq.heappop(store[belong[node]])
                        if active[top]: 
                            heapq.heappush(store[belong[node]], top)
                            answer = top
                            break
                    results.append(answer)
            else: 
                active[node] = False

        return results
