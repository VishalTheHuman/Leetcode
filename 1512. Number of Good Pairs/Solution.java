class Solution {
    public int numIdenticalPairs(int[] nums) {
        int track =0;
        for(int i=0;i<nums.length;i++){
            for(int j=1;j<nums.length;j++){
                if(nums[i]==nums[j] && i<j){
                    track++;
                }
            }
        }
        return track;
    }
}