class Solution {
    public int[] rearrangeArray(int[] nums) {
        int[] pos = new int[nums.length/2];
        int[] neg = new int[nums.length/2];
        int posi = 0;
        int negi = 0;
        for(int i =0;i<nums.length;i++){
            if(nums[i]>0){
                pos[posi]=nums[i];
                posi+=1;
            }else{
                neg[negi]=nums[i];
                negi+=1;
            }
        }
        for(int i =0;i<nums.length/2;i++){
            nums[2*i]=pos[i];
            nums[2*i+1]=neg[i];
        }
        return nums;
    }
}