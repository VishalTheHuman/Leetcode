class Solution {
    public int countAsterisks(String s) {
        int flag = 0;
        int count = 0;
        for(int i =0;i<s.length();i++){
            if(s.charAt(i)=='|'){
                if(flag==0){
                    flag++;
                }else{
                    flag = 0;
                }
                
            }else if(s.charAt(i)=='*' && flag ==0){
                count++;
            }
        }
        return count;
    }
}