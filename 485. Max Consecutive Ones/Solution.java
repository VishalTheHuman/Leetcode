class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int flag =0;
        int flag1=0;
        for(int i=0;i<nums.length;i++){
            if(nums[i]==1){
                flag++;
            }else{
                if(flag>flag1){
                    flag1=flag;
                }
                flag=0;
            }
        }
        if(flag1<flag){
            flag1=flag;
        }
        return flag1;
    }
}