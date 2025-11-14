class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        seen = False

        for i in range(m): 
            if obstacleGrid[i][0] == 1:
                seen = True
            obstacleGrid[i][0] = 0 if seen else 1
        
        seen = False
        

        for i in range(1,n): 
            if obstacleGrid[0][i] == 1:
                seen = True
            obstacleGrid[0][i] = 0 if seen else 1
        
        for i in range(1,m):
            for j in range(1,n): 
                if obstacleGrid[i][j] == 1: 
                    obstacleGrid[i][j] = 0 
                else: 
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
        
        return obstacleGrid[-1][-1]
