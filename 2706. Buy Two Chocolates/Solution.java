class Solution {
    public int buyChoco(int[] prices, int money) {
        int small1,small2;
        if(prices[0]<prices[1]){
            small1 = prices[0];
            small2 = prices[1];
        }else{
            small1 = prices[1];
            small2 = prices[0];
        }
        for(int i=2;i<prices.length;i++){
            if(prices[i]<=small1){
                small2 = small1;
                small1 = prices[i];
            }else if(prices[i]<small2){
                small2 = prices[i];
            }
        }
        if(money-small1-small2>=0){
            return money-small1-small2;
        }
        return money;
    }
}