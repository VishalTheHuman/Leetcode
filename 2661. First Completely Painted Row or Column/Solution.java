class Solution {
    public int firstCompleteIndex(int[] arr, int[][] mat) {
        int m = mat.length; 
        int n = mat[0].length; 
        int[] rows = new int[m]; 
        int[] cols = new int[n]; 

        Map<Integer, int[]> store = new HashMap<>(); 
        
        for(int i=0; i<m;i++){
            for(int j=0;j<n;j++){
                store.put(mat[i][j], new int[]{i,j}); 
            }
        }

        int i, j; 

        for (int k=0; k<arr.length;k++){
            i = store.get(arr[k])[0];
            j = store.get(arr[k])[1];
            rows[i]++;
            cols[j]++;
            if (rows[i]==n || cols[j]==m) return k; 
        }
        return -1; 
    }
}
