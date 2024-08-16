class Solution {
    public int[] sortArrayByParityII(int[] nums) {
        int len = nums.length;
        int[] arr = new int[len];
        int odd = 1;
        int even = 0;
        int i=0;
        while(i<len){
            if(nums[i]%2==0){
                arr[even]=nums[i];
                even+=2;
            }else{
                arr[odd]=nums[i];
                odd+=2;
            }
            i+=1;
        }
        return arr;
    }
}