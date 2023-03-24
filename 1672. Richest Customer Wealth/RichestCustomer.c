int maximumWealth(int** accounts, int accountsSize, int* accountsColSize){
    int sum,wealth=0;
        for(int i=0;i<accountsSize;i++){
            sum=0;
            for(int j=0;j<accountsColSize[i];j++){
                sum+=accounts[i][j];
            }
            if(sum>wealth){
                wealth=sum;
            }
        }
        return wealth;
}