class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        moves = [
            (0,1), 
            (1,0), 
            (0,-1), 
            (-1,0)
        ]
        m, n = len(grid), len(grid[0])
        def traverse(i,j): 
            currSum = 0 
            currSum += grid[i][j]
            grid[i][j] = 0 
            for idx_i, idx_j in moves: 
                idx_i += i 
                idx_j += j
                if 0 <= idx_i < m and 0 <= idx_j < n and grid[idx_i][idx_j]: 
                    currSum += traverse(idx_i,idx_j)
            return currSum
        count = 0 
        for i in range(m): 
            for j in range(n): 
                if grid[i][j] != 0: 
                    count += ((traverse(i,j)%k) == 0)
        return count
