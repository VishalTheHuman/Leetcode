class Solution {
    int[][] world; 
    int[][] moves = {{0,1},{1,0},{0,-1},{-1,0}}; 
    int m,n; 
    public int findMaxFish(int[][] grid) {
        m = grid.length; 
        n = grid[0].length; 
        world = grid;
        int currMax = 0; 
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if (world[i][j]>0){
                    int curr = dfs(i,j); 
                    if (curr > currMax){
                        currMax = curr; 
                    }
                }
            }
        }
        return currMax; 
    }

    public int dfs(int i, int j){
        if(world[i][j]==0){
            return 0; 
        }
        int curr = world[i][j]; 
        world[i][j] = 0; 
        for(int[] move : moves){
            int ci = move[0]+i;
            int cj = move[1]+j; 
            if (0<= ci && ci < m && 0<=cj && cj<n && world[ci][cj]>0){
                curr += dfs(ci,cj); 
            }
        }
        return curr;
    }
}
