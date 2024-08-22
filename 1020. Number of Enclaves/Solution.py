class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        totalOnes = boundaryOnes = 0 
        M, N = len(grid), len(grid[0])
        for i in range(M): 
            for j in range(N): 
                if grid[i][j]:
                    totalOnes += 1
        
        q = deque([])

        for i in range(N):
            if grid[0][i]:
                q.append((0,i))
                grid[0][i] = 0
            if grid[M-1][i]:
                q.append((M-1,i))
                grid[M-1][i] = 0
        
        for i in range(M): 
            if grid[i][0]: 
                q.append((i,0))
                grid[i][0] = 0
            if grid[i][N-1]: 
                q.append((i,N-1))
                grid[i][N-1] = 0

        moves = [
            (0, 1), 
            (1, 0),
            (0,-1), 
            (-1,0)
        ]
        while q: 
            for _ in range(len(q)): 
                i, j = q.popleft()
                boundaryOnes += 1
                for i_c, j_c in moves: 
                    n_i, n_j = i+i_c, j+j_c
                    if 0<=n_i<M and 0<=n_j<N and grid[n_i][n_j] == 1: 
                        grid[n_i][n_j] = 0
                        q.append((n_i,n_j))
        return totalOnes - boundaryOnes
