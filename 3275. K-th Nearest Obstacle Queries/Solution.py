class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        result = []
        count = 0 
        store = []
        elem = 1
        for x, y in queries: 
            heapq.heappush(store, - (abs(x)+abs(y)))
            if len(store) > k: 
                heapq.heappop(store)
            if len(store) == k:
                elem = heapq.heappop(store)
                heapq.heappush(store, elem)
                
            result.append(-elem)
        
        return result
