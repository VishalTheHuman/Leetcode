class Solution {
    public int maxProduct(int[] nums) {
        int large,large2;
        if(nums[0]>nums[1]){
            large = nums[0];
            large2 =nums[1];
        }else{
            large = nums[1];
            large2 = nums[0];
        }
        for(int i=2;i<nums.length;i++){
            if(nums[i]>=large){
                large2 = large;
                large = nums[i];
            }else if(nums[i]>large2){
                large2 = nums[i];
            }
        }
        return(large-1)*(large2-1);
    }
}