class Solution {
    public int arraySign(int[] nums) {
        double product = 1;
        for(int i=0;i<nums.length;i++){
            product*=nums[i];
        }
        return signFunc(product); 
    }
    public int signFunc(double x){
        if(x<0){
            return -1;
        }else if(x>0){
            return 1;
        }
        return 0;
    }
}