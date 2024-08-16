class Solution {
    public boolean isPalindrome(String s) {
        String r="";
        for(int i=0;i<s.length();i++){
            int temp = s.charAt(i);
            if((temp>=65 && temp<=90) || (temp>=97 && temp<=122 || (temp>=48 && temp<=57))){
                r=r + s.charAt(i);
            }
        }
        r = r.toLowerCase();
        for(int i=0;i<r.length()/2;i++){
            if(r.charAt(i)!=r.charAt(r.length()-1-i)){
                return false;
            }
        }
        return true;
    }
}
