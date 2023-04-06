class Solution {
    public boolean checkXMatrix(int[][] grid) {
        int j=grid.length-1;
        for(int i=0;i<grid.length;i++){
            if(grid[i][i]==0){
                return false;
            }else if(grid[i][j]==0){
                return false;
            }
            for(int k=0;k<grid.length;k++){
                if(k!=j && k!=i && grid[i][k]!=0){
                    return false;
                }
            }
            j--;
        }
        return true;
    }
}