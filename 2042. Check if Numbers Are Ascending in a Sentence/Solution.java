class Solution {
    public boolean areNumbersAscending(String s) {
        int less = -1;
        for(String x : s.split(" ")){
            try{
                if(Integer.parseInt(x)>less){
                    less = Integer.parseInt(x);
                }else{
                    return false;
                }
            }catch(NumberFormatException e){
                continue;
            }
        }
        return true;
    }
}