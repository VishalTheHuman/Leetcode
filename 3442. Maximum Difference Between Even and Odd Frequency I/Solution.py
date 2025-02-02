class Solution:
    def maxDifference(self, s: str) -> int:
        store = Counter(s)
        diff = 0 
        odd, even = [], []
        for x in sorted(set(store.values())):
            if x%2==1: 
                odd.append(x)
            else:
                even.append(x)
        return odd[-1]-even[0]
