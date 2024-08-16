class Solution {
    public boolean isMonotonic(int[] nums) {
        if(nums.length<=2){
            return true;
        }
        int flag= nums[0];
        int DorA = 0;
        for(int i=1;i<nums.length;i++){
            if(DorA>0){
                if(nums[i]-flag>=0){
                    DorA = 1;
                }else{
                    return false;
                }
            }else if(DorA<0){
                if(nums[i]-flag<=0){
                    DorA = -1;
                }else{
                    return false;
                }
            }else{
                if(nums[i]-flag>0){
                    DorA = 1;
                }else if(nums[i]-flag<0){
                    DorA = -1;
                }
            }
            flag = nums[i];
        }
        return true;
    }
}