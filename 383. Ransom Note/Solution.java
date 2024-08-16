class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        if(ransomNote.length()>magazine.length()) return false;
        int[] arr = new int[26];
        for(int i=0;i<magazine.length();i++){
            arr[magazine.charAt(i)-'a']+=1;
        }
        for(int i=0;i<ransomNote.length();i++){
            if(arr[ransomNote.charAt(i)-'a']==0){
                return false;
            }else{
                arr[ransomNote.charAt(i)-'a']-=1;
            }
        }
        return true;
    }
}