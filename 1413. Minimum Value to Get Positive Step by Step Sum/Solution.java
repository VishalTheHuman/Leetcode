class Solution {
    public int minStartValue(int[] nums) {
        int sum=0;
        int startValue =1;
        while(sum<1){
            sum = startValue;
            for(int i=0;i<nums.length;i++){
                sum+=nums[i];
                if(sum<1){
                    startValue++;
                    break;
                }
            }
        }
        return startValue;
    }
}