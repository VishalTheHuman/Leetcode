class Solution {
    public int countAsterisks(String s) {
        int flag = 0;
        int count = 0;
        for(char c : s.toCharArray()){
            if(c=='|'){
                flag++;
            }else if(c=='*' && flag%2 ==0){
                count++;
            }
        }
        return count;
    }
}