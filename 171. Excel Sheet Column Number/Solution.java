class Solution {
    public int titleToNumber(String columnTitle) {
        int sum=0;
        int flag;
        for(int i= 0;i<columnTitle.length();i++){
            flag = (int) columnTitle.charAt(i) - 64;
            sum = sum*26 + flag;
        }
        return sum;
    }
}