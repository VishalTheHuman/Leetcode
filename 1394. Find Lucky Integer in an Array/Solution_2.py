class Solution:
    def findLucky(self, arr: List[int]) -> int:
        dt = Counter(arr)
        l = []
        for k,v in dt.items():
            if k==v:
                l.append(k)
        return -1 if not l else max(l)
