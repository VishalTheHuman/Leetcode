class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        temp = Counter(s)
        return abs(temp.get("a", 0)-temp.get("b", 0))
