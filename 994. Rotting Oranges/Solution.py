class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque([])
        M, N, fresh = len(grid), len(grid[0]), 0
        for i in range(M): 
            for j in range(N): 
                if grid[i][j] == 2: 
                    grid[i][j] = 3
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        moves = [
            (0, 1), 
            (0,-1), 
            (-1,0),
            (1, 0)
        ]
        minutes = 0
        while fresh and queue:
            change = 0
            for _ in range(len(queue)):
                i,j = queue.popleft()
                for i_c, j_c in moves: 
                    if 0<= (i+i_c) < M and 0<= (j+j_c) < N and grid[i+i_c][j+j_c]==1:
                        queue.append((i+i_c, j+j_c))
                        change += 1
                        grid[i+i_c][j+j_c] = 3
            if change == 0:
                break
            fresh -= change
            minutes += 1
        if fresh == 0:
            return minutes
        return -1
