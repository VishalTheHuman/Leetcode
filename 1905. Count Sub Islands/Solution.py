class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        moves = [
            (0, 1), 
            (1, 0), 
            (-1,0), 
            (0,-1)
        ]

        M, N = len(grid1), len(grid1[0])

        def dfs(i, j):
            nonlocal M, N
            
            if grid1[i][j] == 0:
                return False

            grid2[i][j] = 0
            possible = True
            for i_c, j_c in moves: 
                if 0<=(i+i_c)<M and 0<=(j+j_c)<N and grid2[i+i_c][j+j_c]: 
                    if not dfs(i+i_c, j+j_c): 
                        possible = False

            return possible

        count = 0 
        for i in range(M): 
            for j in range(N): 
                if grid2[i][j]:
                    if dfs(i,j): 
                        count += 1

        return count
