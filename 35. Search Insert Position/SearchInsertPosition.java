class Solution {
    public int searchInsert(int[] nums, int target) {
    int index=0;
    for(int i=0;i<nums.length;i++)
    {
        if(nums[i]<target){
            index++;
        }else{
            return index;
        }
    }
    if(index>0){
        return index;
    }
    else{
        return 0;
    }
}
}