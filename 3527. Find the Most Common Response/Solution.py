class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        overall = defaultdict(int)
        seen = set()
        for idx in range(len(responses)): 
            seen.clear()
            for x in responses[idx]: 
                if x in seen: 
                    continue
                overall[x] += 1
                seen.add(x)
        maxCommonCount = max(overall.values())
        return sorted(list(
            filter(lambda x : x[1]==maxCommonCount, 
            overall.items())
        ))[0][0]
