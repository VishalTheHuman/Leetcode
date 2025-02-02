class Solution {
    public boolean check(int[] nums) {
        int smallest = 101; 
        int index = -1; 
        int n = nums.length; 
        for(int i=0;i<n;i++){
            if(smallest > nums[i]){
                index = i; 
                smallest = nums[i]; 
            }else if(smallest==nums[i]){
                if (nums[i-1]!=nums[i]){
                    index = i; 
                    smallest = nums[i];
                }
            }
        }

        for(int i=index; i<(index + n -1); i++){
            if (nums[(i)%n] > nums[(i+1)%n]){
                return false; 
            }
        }
        return true; 
    }
}
