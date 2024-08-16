class Solution {
    public int maximumCount(int[] nums) {
        int negative=0,positive=0;
        for(int i=0;i<nums.length;i++){
            if(nums[i]<0){
                negative++;
            }else if(nums[i]>0){
                positive++;
            }
        }
        if(negative>positive){
            return negative;
        }else{
            return positive;
        }
    }
}