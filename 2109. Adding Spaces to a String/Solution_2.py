class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = "
        j = 0
        for i in range(len(s)):
            if j < len(spaces) and i == spaces[j]:
                result += 

                j += 1
            result += s[i]
        return result
