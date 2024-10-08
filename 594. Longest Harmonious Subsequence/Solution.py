class Solution:
    def findLHS(self, nums: List[int]) -> int:
        store = sorted(Counter(nums).items())
        maxSequence = 0
        for i in range(1, len(store)):
            if (store[i][0] - store[i-1][0]) == 1:
                maxSequence = max(maxSequence,store[i][1] + store[i-1][1] )
        return maxSequence
