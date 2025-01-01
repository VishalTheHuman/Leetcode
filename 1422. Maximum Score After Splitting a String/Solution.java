class Solution {
    public int maxScore(String s) {
        int currMax = 0;
        int ones = 0, zeros = 0; 
        for(char x : s.toCharArray()){
            if(x=='1'){
                ones++; 
            }else{
                zeros++; 
            }
        }
        int currZeros = 0; 
        for(int i=0;i<s.length()-1;i++){
            char x = s.charAt(i);
            if(x=='0'){
                currZeros++;
            }else if (x=='1'){
                ones--; 
            }
            currMax = Math.max(currMax, currZeros + ones);
        }
        return currMax; 
    }
}
