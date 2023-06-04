class Solution {
    public boolean divideArray(int[] nums) {
        int[] freq = new int[501];
        for(int x:nums){
            freq[x]+=1;
        }
        for(int x:nums){
            if(freq[x]%2!=0){
                return false;
            }
        }
        return true;
    }
}