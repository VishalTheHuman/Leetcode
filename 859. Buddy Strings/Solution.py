class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal): return False
        indices = []
        for i in range(len(s)):
            if s[i]!=goal[i]:
                indices.append(i)
            if len(indices) > 2: 
                return False
        if len(indices) == 0:
            seen = set()
            for x in s:
                if x in seen:
                    return True
                seen.add(x)
            return False
        elif len(indices) == 1:
            return False
        return s[indices[0]] == goal[indices[1]] and s[indices[1]] == goal[indices[0]]
