class Solution {
    public int maximumWealth(int[][] accounts) {
        int sum,wealth=0;
        for(int i=0;i<accounts.length;i++){
            sum=0;
            for(int j=0;j<accounts[i].length;j++){
                sum+=accounts[i][j];
            }
            if(sum>wealth){
                wealth=sum;
            }
        }
        return wealth;
    }
}