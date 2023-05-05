class Solution {
    public int[] rowAndMaximumOnes(int[][] mat) {
        int ones = 0;
        int[] high= new int[2];
        for(int i=0;i<mat.length;i++){
            ones=0;
            for(int j=0;j<mat[i].length;j++){
                if(mat[i][j]==1){
                    ones++;
                }
            }
            if(ones>high[1]){
                high[0] = i;
                high[1] = ones; 
            }
        }
        return high;
    }
}