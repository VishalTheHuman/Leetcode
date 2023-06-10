class Solution {
    public boolean areOccurrencesEqual(String s) {
        int[] arr = new int[26];
        int i =0;
        for(i=0;i<s.length();i++){
            arr[s.charAt(i)-'a'] +=1;
        }
        Arrays.sort(arr);
        for(i=25;i>=1;i--){
            if(arr[i-1]==0) return true;
            if(arr[i]!=arr[i-1]) return false;
        }
        return true;
    }
}