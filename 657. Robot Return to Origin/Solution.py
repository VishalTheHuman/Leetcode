class Solution:
    def judgeCircle(self, moves: str) -> bool:
        store = {
            "D" : (-1,0), 
            "U" : (1, 0), 
            "R" : (0, 1), 
            "L" : (0,-1)
        }
        X = Y = 0
        for m in moves: 
            x, y = store[m]
            X += x
            Y += y
        return X==0 and Y==0
