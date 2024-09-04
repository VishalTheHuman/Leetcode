class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        rowStore = defaultdict(set)
        colStore = defaultdict(set)
        direction = {
            0 : (1, 0), # R
            1 : (0,-1), # D
            2 : (-1, 0), # L
            3 : (0,1) # U
        }

        for x, y in obstacles:
            rowStore[x].add(y)
            colStore[y].add(x)

        pX = pY = maxDistance = 0
        D = 3 
        x, y = direction[D]
        for c in commands:
            if c == -1:
                D = (D+1)%4
                x, y = direction[D]
            elif c == -2: 
                D = (D+3)%4
                x, y = direction[D]
            else: 
                if x: 
                    itr = range(pX+1, pX+c+1) if x == 1 else range(pX-1, pX-c-1, -1)
                    for move in itr: 
                        if move in colStore[pY]:
                            break
                        pX = move
                else: 
                    
                    itr = range(pY+1, pY+c+1) if y == 1 else range(pY-1, pY-c-1, -1)
                    for move in itr: 
                        if move in rowStore[pX]:
                            break
                        pY = move
                maxDistance = max(maxDistance, pX**2+pY**2)
        return maxDistance
