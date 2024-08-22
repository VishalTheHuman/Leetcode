class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        M, N = len(board), len(board[0])

        q = deque([])
        for i in range(N):
            if board[0][i] == "O":
                q.append((0,i))
            if board[M-1][i] == "O":
                q.append((M-1,i))
        
        for i in range(M): 
            if board[i][0] == "O": 
                q.append((i,0))
            if board[i][N-1] == "O": 
                q.append((i,N-1))
        
        moves = [
            (0, 1), 
            (1, 0), 
            (0,-1), 
            (-1,0)
        ]
        while q: 
            for _ in range(len(q)): 
                i,j = q.popleft()
                board[i][j] = "."
                for i_c, j_c in moves: 
                    n_i, n_j = i+i_c, j+j_c
                    if 0<=n_i< M and 0<=n_j<N and board[n_i][n_j] == "O": 
                        q.append((n_i,n_j))
        
        for i in range(M): 
            for j in range(N): 
                if board[i][j] == "O" :
                    board[i][j] = "X"
                elif board[i][j] == ".": 
                    board[i][j] = "O"
