class Solution {
    public int minElement(int[] nums) {
        int minimum = 100000;
        for(int i=0;i<nums.length;i++){
            minimum = Math.min(minimum, reduceNum(nums[i]));
        }
        return minimum;
    }

    public int reduceNum(int num){
        int sum = 0; 
        while(num > 0){
            sum += num%10; 
            num /= 10;
        }
        return sum; 
    }
}
