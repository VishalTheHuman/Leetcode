class Solution:
    def findLucky(self, arr: List[int]) -> int:
        dt = Counter(arr)
        l = -1
        for k,v in dt.items():
            if k==v:
                l = max(l,k)
        return l
