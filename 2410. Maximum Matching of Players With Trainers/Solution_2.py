class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        heapq.heapify(players)
        heapq.heapify(trainers)
        count = 0 
        while len(players) > 0 and len(trainers) > 0: 
            p = heapq.heappop(players)
            while len(trainers) > 0: 
                if p <= heapq.heappop(trainers): 
                    count += 1
                    break
        return count
