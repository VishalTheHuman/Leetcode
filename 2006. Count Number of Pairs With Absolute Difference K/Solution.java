class Solution {
    public int countKDifference(int[] nums, int k) {
        int count = 0;
        for(int j=0;j<nums.length;j++){
            for(int i=0;i<j;i++){
                if(Math.abs(nums[i]-nums[j])==k){
                    count++;
                }
            }
        }
        return count;
    }
}