class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        prev = 0
        result = []
        for idx in spaces:
            result.append(s[prev:idx])
            prev = idx
        result.append(s[spaces[-1]:])
        return " ".join(result)
