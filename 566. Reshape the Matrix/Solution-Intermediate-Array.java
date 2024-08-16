class Solution {
    public int[][] matrixReshape(int[][] mat, int r, int c) {
        if(mat.length * mat[0].length != r*c){
            return mat;
        }
        int matrix[][] = new int[r][c];
        int mat1[] = new int[r*c];
        int k=0;
        for(int i=0;i<mat.length;i++){
            for(int j=0;j<mat[i].length;j++){
                mat1[k]=mat[i][j];
                k++;
            }
        }
        k=0;
        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                matrix[i][j]=mat1[k];
                k++;
            }
        }
        return matrix;
    }
}