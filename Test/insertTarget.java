public class insertTarget {
    public static void main(String[] args) {
        int nums[]={1,2,3,4};
        System.out.println(searchInsert(nums, 8));
    }
    static int searchInsert(int[] nums, int target) {
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