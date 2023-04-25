class Solution {
    public int[][] matrixReshape(int[][] mat, int r, int c) {
        if(mat.length * mat[0].length != r*c){
            return mat;
        }
        int matrix[][] = new int[r][c];
        int a=0,b=0;
        for(int i=0;i<mat.length;i++){
            if(a==r && b==c){
                break;
            }
            for(int j=0;j<mat[i].length;j++){
                matrix[a][b]=mat[i][j];
                b++;
                if(b==c){
                    b=0;
                    a++;
                }
            }
        }
        return matrix;
    }
}