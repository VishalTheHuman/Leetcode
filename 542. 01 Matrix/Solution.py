class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        M, N  = len(mat), len(mat[0])
        MAXINT = 10**5
        store = [[MAXINT]*N for _ in range(M)] 
        visited = [[False]*N for _ in range(M)]

        queue = deque([])

        for i in range(M): 
            for j in range(N): 
                if mat[i][j] == 0: 
                    queue.append((i,j,0))
                    visited[i][j] = True
        
        moves = [
            (0, 1), 
            (1, 0), 
            (0,-1), 
            (-1,0)
        ]

        while queue: 
            for _ in range(len(queue)): 
                i,j, dis = queue.popleft()
                store[i][j] = dis
                for i_c, j_c in moves: 
                    if 0<=(i+i_c)< M and 0<=(j+j_c)<N:
                        if visited[i+i_c][j+j_c]: 
                            continue
                        visited[i+i_c][j+j_c] = True
                        queue.append((i+i_c, j+j_c, dis + 1))

        return store
