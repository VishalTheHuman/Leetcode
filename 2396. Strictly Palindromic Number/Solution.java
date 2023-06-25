class Solution {
    public boolean isStrictlyPalindromic(int n) {
        for(int i=2;i<=n-2;i++){
            if(!isPalindrome(convertBase(n,i))){
                return false;
            }
        }
        return true;
    }
    public String convertBase(int n,int base){
        StringBuilder ret = new StringBuilder();
        while(n>0){
            int modulo = n%base;
            n/=base;
            ret.insert(0,Integer.toString(modulo));
        }
        return ret.toString();
    }
    public boolean isPalindrome(String s){
        int n=s.length();
        for(int i=0;i<s.length()/2;i++){
            if(s.charAt(i)!=s.charAt(n-1-i)) return false;
        }
        return true;
    }
}