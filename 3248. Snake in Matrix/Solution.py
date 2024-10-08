class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        matrix = [[0]*n for i in range(n)]
        val = 0
        for i in range(n):
            for j in range(n):
                matrix[i][j] = val
                val+=1
        
        moves = {
            "UP" : (-1,0),
            "DOWN" : (1,0), 
            "RIGHT" : (0,1), 
            "LEFT" : (0, -1)
        }
        i, j = 0, 0
        for move in commands:
            i_c, j_c = moves[move]
            i += i_c
            j += j_c
        return matrix[i][j]
            
