class Solution {
    int[] isConnected;
    public int[] findRedundantConnection(int[][] edges) {
        int m = edges.length; 
        isConnected = new int[m];

        for(int i=0;i<m;i++){
            isConnected[i] = i;
        }
        
        for(int[] edge : edges){
            int x = edge[0]-1; 
            int y = edge[1]-1; 
            if (find(x)==find(y)){
                return edge; 
            }
            union(x,y); 
        }

        return new int[]{}; 
    }

    public void union(int x, int y){
        isConnected[find(x)] = find(y); 
    }

    public int find(int x){
        if(isConnected[x]==x){
            return x;
        }
        isConnected[x] = find(isConnected[x]); 
        return isConnected[x];
    }
}
