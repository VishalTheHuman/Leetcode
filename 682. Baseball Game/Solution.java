class Solution {
    public int calPoints(String[] operations) {
        Stack<Integer> ret = new Stack<>();
        for(String x : operations){
            if(x.equals("C")){
                ret.pop();
            }else if(x.equals("D")){
                int temp = 2*ret.peek();
                ret.push(temp);
            }else if(x.equals("+")){
                if(!ret.empty()){
                    int temp = ret.pop();
                    if(!ret.empty()){
                        int temp1 = ret.peek();
                        ret.push(temp);
                        ret.push(temp+temp1);
                    }else{
                        ret.push(temp);
                    }
                }
            }else{
                ret.push(Integer.parseInt(x));
            }
        }
        int count = 0;
        while(!ret.empty()){
            count+=ret.pop();
        }
        return count;
    }
}