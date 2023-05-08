class Solution {
    public boolean checkString(String s) {
        int flag = 0;
        for(int i =0;i<s.length();i++){
            if(s.charAt(i)=='b'){
                flag = 1;
            }
            if(flag==1 && s.charAt(i)=='a'){
                return false;
            }
        }
        return true;
    }
}