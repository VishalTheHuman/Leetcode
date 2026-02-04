class Solution:
    def maxPoints(self, technique1: List[int], technique2: List[int], k: int) -> int:
        reward = 0 
        temp = []
        n = len(technique1)

        for idx in range(n): 
            temp.append((
                technique2[idx] - technique1[idx], 
                technique1[idx], 
                technique2[idx]
            ))

        heapq.heapify(temp)

        idx = 0 

        while k:
            _, r1, _ = heapq.heappop(temp)
            reward += r1
            k-=1
        
        while len(temp): 
            _, r1, r2 = heapq.heappop(temp)
            reward += max(r1, r2)

        return reward 
