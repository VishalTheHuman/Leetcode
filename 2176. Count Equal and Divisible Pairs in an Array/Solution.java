class Solution {
    public int countPairs(int[] nums, int k) {
        int count = 0;
        for(int j=0;j<nums.length;j++){
            for(int i=0;i<j;i++){
                if(nums[i]==nums[j]){
                    if((i*j)%k==0){
                        count++;
                    }
                }
            }
        }
        return count;
    }
}