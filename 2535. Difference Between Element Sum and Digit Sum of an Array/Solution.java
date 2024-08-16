class Solution {
    public int differenceOfSum(int[] nums) {
        int elsum = 0;
        int disum = 0;
        for(int i=0;i<nums.length;i++){
            elsum+=nums[i];
            int size = (int) Math.log10(nums[i]) +1;
            if(size>1){
                for(int j=0;j<size;j++){
                    disum += nums[i]%10;
                    nums[i]/=10;
                }
            }else{
                disum+=nums[i];
            }
        }
        return (int) Math.abs(elsum-disum);
    }
}