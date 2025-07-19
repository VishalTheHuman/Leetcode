class Solution:
    def partitionString(self, s: str) -> List[str]:
        seen = set()
        order = []
        curr = ""
        for i in range(len(s)): 
            curr += s[i]
            if curr not in seen: 
                seen.add(curr)
                order.append(curr)
                curr = ""
        return order
