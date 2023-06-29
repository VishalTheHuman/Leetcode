class Solution {
    public int[] sortArrayByParity(int[] nums) {
        int start_index = 0;
        for(int i=0;i<nums.length;i++){
            if(nums[i]%2==0){
                int temp = nums[i];
                nums[i]=nums[start_index];
                nums[start_index]=temp;
                start_index+=1;
            }
        }
        return nums;
    }
}