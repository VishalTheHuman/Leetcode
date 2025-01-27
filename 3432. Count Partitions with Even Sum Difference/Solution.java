class Solution {
    public int countPartitions(int[] nums) {
        int count = 0; 
        int n = nums.length; 
        for(int i=1; i<n;i++){
            nums[i]+=nums[i-1]; 
        }
        for(int i=0;i<n-1;i++){
            if(Math.abs(nums[i] - (nums[n-1]-nums[i]))%2==0){
                count++;
            }
        }
        return count; 
    }
}
