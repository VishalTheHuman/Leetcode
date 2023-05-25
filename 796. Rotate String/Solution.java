class Solution {
    public boolean rotateString(String s, String goal) {
        StringBuilder ret = new StringBuilder(s);
        for(int i=0;i<s.length();i++){
            if(ret.toString().equals(goal)){
                return true;
            }
            char temp = ret.charAt(0);
            ret.deleteCharAt(0);
            ret.append(temp);
        }
        return false;
    }
}