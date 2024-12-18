class Solution {
    public int[] finalPrices(int[] prices) {
        Stack<ValIdx> stack = new Stack<>(); 
        for(int i=0;i<prices.length;i++){
            while(!stack.empty() && stack.peek().val >= prices[i]){
                ValIdx temp = stack.pop();
                prices[temp.idx] = temp.val - prices[i]; 
            }
            stack.push(new ValIdx(prices[i], i));
        }
        return prices; 
    }
}

class ValIdx{
    int val, idx; 
    public ValIdx(int val, int idx){
        this.val = val; 
        this.idx = idx; 
    }
}
