class Solution {
    public long findTheArrayConcVal(int[] nums) {
        long sum = 0;
        int i = 0;
        int j = nums.length-1;
        if(nums.length%2==1){
            sum =nums[(int) Math.ceil(nums.length/2)];
        }
        while(i<j){
            sum+=Integer.parseInt((Integer.toString(nums[i])+Integer.toString(nums[j])));
            i++;
            j--;
        }
        return sum;
    }
}