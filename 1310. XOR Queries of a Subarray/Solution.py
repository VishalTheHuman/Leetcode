class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = [0, arr[0]]
        for i in range(1, len(arr)): 
            prefix.append(prefix[-1]^arr[i])
        result = []
        for x, y in queries: 
            result.append(prefix[y+1]^prefix[x])
        return result
