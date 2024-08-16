class Solution {
    public int balancedStringSplit(String s) {
        int R=0;
        int L=0;
        int count =0;
        for(int i=0;i<s.length();i++){
            if(s.charAt(i)=='R'){
                R++;
            }else{
                L++;
            }
            if(L==R && L>0 && R>0){
                count++;
                L=0;
                R=0;
            }
        }
        return count;
    }
}