class Solution {
    public int totalMoney(int n) {
        int sum = 0;
        int count = 0;
        int flag = 0;
        while(count<=n){
            flag+=1;
            for(int i = 0;i<7;i++){
                if(count==n){
                    return sum;
                }
                sum+=(i+flag);
                count++;
            }
        }
        return sum;
    }
}