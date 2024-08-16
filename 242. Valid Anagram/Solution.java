class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length()!=t.length()) return false;
        int[] arr = new int[26];
        int i;
        for(i=0;i<s.length();i++){
            arr[s.charAt(i)-'a']+=1;
        }
        for(i=0;i<t.length();i++){
            arr[t.charAt(i)-'a']-=1;
        }
        for(i=0;i<26;i++){
            if(arr[i]!=0){
                return false;
            }
        }
        return true;
    }
}