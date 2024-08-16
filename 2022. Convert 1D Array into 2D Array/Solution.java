class Solution {
    public int[][] construct2DArray(int[] original, int m, int n) {
        int[][] matrix = new int[m][n];
        int k=0;
        int[][] emp = new int[][]{};
        if(original.length>m*n || original.length<m*n){
            return emp;
        }
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                matrix[i][j]=original[k];
                k++;
            }
        }
        return matrix;
    }
}