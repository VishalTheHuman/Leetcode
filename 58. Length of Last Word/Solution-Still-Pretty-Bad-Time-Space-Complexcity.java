class Solution {
    public int lengthOfLastWord(String s) {
        int  len = 0;
        s = s.strip();
        for(int x = 0;x<s.length();x++){
            if(s.charAt(x)!=' '){
                len++;
            }else{
                len=0;
            }
        }
        return len;
    }
}