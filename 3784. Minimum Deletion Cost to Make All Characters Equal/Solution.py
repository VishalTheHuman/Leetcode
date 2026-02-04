class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        char_cost = defaultdict(int)
        total = 0 
        for idx in range(len(s)): 
            total += cost[idx]
            char_cost[s[idx]] += cost[idx]
        if len(char_cost) == 1: 
            return 0 
        return total - max(char_cost.values())
