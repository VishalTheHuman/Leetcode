class Solution {
    public boolean isBalanced(String num) {
        int oddSum = 0, evenSum = 0; 
        for(int i=0;i<num.length();i+=2){
            evenSum += ((int) num.charAt(i) - (int) 0);
        }
        for(int i=1;i<num.length();i+=2){
            oddSum += ((int) num.charAt(i) - (int) 0);
        }
        return oddSum == evenSum;
    }
}
