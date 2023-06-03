class Solution {
    public int removeDuplicates(int[] nums) {
        List<Integer> ret = new ArrayList<>();
        int j=0;
        for(int i=0;i<nums.length;i++){
            if(ret.indexOf(nums[i])==-1){
                ret.add(nums[i]);
                nums[j]=nums[i];
                j++;
            }
        }
        return j;
    }
}