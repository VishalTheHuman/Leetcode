int search(int* nums, int numsSize, int target){
    int start =0;
    int end = numsSize-1;
    int mid = (numsSize-1)/2;
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