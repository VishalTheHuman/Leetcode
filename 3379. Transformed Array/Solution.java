class Solution {
    public int[] constructTransformedArray(int[] nums) {
        int length = nums.length;
        int[] result = new int[length];
        for(int i=0;i<length;i++){
            if(nums[i]==0){
                result[i] = nums[i]; 
            }else if (nums[i] > 0){
                result[i] = nums[(i+nums[i])%length]; 
            }else{
                result[i] = nums[(length + i - (Math.abs(nums[i]) % length))%length];
            }
        }
        return result; 
    }
}
