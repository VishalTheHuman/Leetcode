class Solution {
    public int[][] sortMatrix(int[][] grid) {
        // lower
        for(int i=grid.length-1;i>=0;i--){
            ArrayList<Integer> temp = new ArrayList<>(); 
            for(int j=0;j<grid.length-i;j++){
                temp.add(grid[i+j][j]); 
            }
            Collections.sort(temp, Collections.reverseOrder());
            int curr = 0; 
            for(int j=0;j<grid.length-i;j++){
                grid[i+j][j] = temp.get(curr);
                curr++; 
            }
        }
        // upper
        for(int j=1;j<grid.length;j++){
            ArrayList<Integer> temp = new ArrayList<>(); 
            for(int i=0;i<grid.length-j;i++){
                temp.add(grid[i][j+i]); 
            }
            Collections.sort(temp);
            int curr = 0; 
            for(int i=0;i<grid.length-j;i++){
                grid[i][j+i] = temp.get(curr);
                curr++; 
            }
        }
        return grid;
    }
}
