class Solution {
    public int removeElement(int[] nums, int val) {
        int count = 0;
        int i =0;
        while(true){
            if(i==nums.length-count) break;
            if(nums[i]==val){
                int temp = nums[i];
                nums[i] = nums[nums.length-1-count];
                nums[nums.length-1-count] = temp;
                count+=1;
                continue;
            }
            i+=1;
        }        
        return nums.length-count;
    }
}