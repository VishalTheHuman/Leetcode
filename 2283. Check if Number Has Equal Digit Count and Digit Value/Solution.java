class Solution {
    public boolean digitCount(String num) {
        int[] integers = new int[10];
        for(int i=0;i<num.length();i++){
            integers[num.charAt(i)-'0']+=1;
        }
        for(int i=0;i<num.length();i++){
            if((num.charAt(i)-'0')!=integers[i]){
                return false;
            }
        }
        return true;
    }
}