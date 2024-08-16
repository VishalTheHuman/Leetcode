class Solution {
    public int equalPairs(int[][] grid) {
        int count = 0;
        boolean flag;
        int[] ret = new int[grid.length];
        for(int i=0;i<grid.length;i++){
            for(int j=0;j<grid.length;j++){
                ret[j] = grid[i][j];
            }
            for(int k=0;k<grid.length;k++){
                flag = true;
                for(int j=0;j<grid.length;j++){
                    if(ret[j]!=grid[j][k]){
                        flag =false;
                        break;
                    }
                }
                if(flag==true){
                    count+=1;
                }
            }
        }
        return count;
    }
}