class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int m = matrix.length, n = matrix[0].length; 
        int row = m-1; 

        // row
        int start = 0; 
        int end = m; 
        int mid = -1; 
        while (start < end && start < m && end >=0){
            mid = (start + end) / 2; 
            if (matrix[mid][0] <= target){
                if (matrix[mid][n-1]>=target){
                    row = mid; 
                    break; 
                }else{
                    start = mid+1; 
                }
            }else{
                end = mid; 
            }
        }
        start = 0; 
        end = n;

        while(start <= end && end >=0 && start < n){
            mid = (start+end)/2; 
            if(matrix[row][mid]==target){
                return true; 
            }else if (matrix[row][mid]<target){
                start = mid+1;
            }else{
                end = mid-1; 
            }
        }
        
        return false; 
    }
}
