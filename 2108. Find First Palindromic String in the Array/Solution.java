class Solution {
    public String firstPalindrome(String[] words) {
        for(int i=0;i<words.length;i++){
            if(words[i].length()==1){
                return words[i];
            }
            if(ispali(words[i])){
                return words[i];
            }
        }
        return "";
    }
    public boolean ispali(String s){
        for(int i=0;i<s.length();i++){
            if(s.charAt(i)!=s.charAt(s.length()-1-i)){
                return false;
            }
        }
        return true;
    }
}