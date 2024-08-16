class Solution {
    public String makeSmallestPalindrome(String s) {
        char[] arr = s.toCharArray();
        for(int i=0,j=arr.length-1;i<j;i++,j--){
            arr[i]=arr[j]=(char)Math.min(arr[i],arr[j]);
        }
        return new String(arr);
    }
}