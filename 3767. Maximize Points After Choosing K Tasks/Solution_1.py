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

        temp.sort(key = lambda x : x[0])

        idx = 0 

        while k:
            reward += temp[idx][1]
            idx += 1
            k-=1
        
        while idx < n: 
            reward += max(
                temp[idx][1], 
                temp[idx][2]
            )
            idx += 1
        
        return reward 
