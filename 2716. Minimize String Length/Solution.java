class Solution {
    public int minimizedStringLength(String s) {
        int[] arr = new int[26];
        for(int i=0;i<s.length();i++){
            arr[s.charAt(i)-'a']+=1;
        }
        int count=0;
        for(int i=0;i<26;i++){
            if(arr[i]>0) count+=1;
        }
        return count;
    }
}