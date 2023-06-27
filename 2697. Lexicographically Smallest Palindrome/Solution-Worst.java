class Solution {
    public String makeSmallestPalindrome(String s) {
        StringBuilder ret = new StringBuilder();
        int len = s.length();
        int j =0;
        for(int i=0;i<len/2;i++){
            if(s.charAt(i)!=s.charAt(len-1-i)){
                if(s.charAt(i)<s.charAt(len-1-i)){
                    ret.insert(j,s.charAt(i));
                    ret.insert(j,s.charAt(i));
                }else{
                    ret.insert(j,s.charAt(len-1-i));
                    ret.insert(j,s.charAt(len-1-i));
                }
            }else{
                ret.insert(j,s.charAt(len-i-1));
                ret.insert(j,s.charAt(i));
            }
            j+=1;
        }
        if(len%2!=0){
            ret.insert(j,s.charAt(j));
        }
        return ret.toString();
    }
}