class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x = sorted(Counter(nums).items(), key = lambda x : x[1], reverse=True)[:k]
        return [y[0] for y in x]
