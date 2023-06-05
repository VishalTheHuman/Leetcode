class Solution {
    public int[] twoSum(int[] nums, int target) {
        int c = 1;
        while(true){
            for(int i=0;i<nums.length-c;i++){
                if(nums[i]+nums[c+i]==target){
                    return new int[]{i,i+c};
                }
            }
            c++;
        }
    }
}