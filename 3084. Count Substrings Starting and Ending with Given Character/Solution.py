class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        indices = []
        for idx,ch in enumerate(s):
            if ch==c:
                indices.append(idx)
        total = len(indices)
        return (total * (total+1)) //2
