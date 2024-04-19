class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0 
        seen = set()
        m, n = len(grid), len(grid[0])
        def dfs(i,j):
            nonlocal seen, m, n
            seen.add((i,j))
            moves = [
                (1,0), 
                (0,1),
                (-1,0),
                (0,-1)
            ]
            for (m_i, m_j) in moves:
                m_i += i
                m_j += j
                if 0 <= m_i < m and 0 <= m_j < n and (m_i, m_j) not in seen and grid[m_i][m_j]=="1":
                    dfs(m_i, m_j)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in seen:
                    dfs(i,j)
                    islands += 1
        return islands
