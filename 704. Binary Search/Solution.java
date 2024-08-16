class Solution {
    public int search(int[] nums, int target) {
        int start =0;
        int end = nums.length-1;
        int mid = (nums.length-1)/2;
        while(true){
            int mid1=mid;
            if(nums[mid]==target){
                return mid;
            }else if(nums[mid]<target){
                start = mid+1;
                mid=(start+end)/2;
            }else if(nums[mid]>target){
                end = mid-1;
                mid = (start+end)/2;
            }
            if(mid1==mid){
                return -1;
            }
        }
    }
}