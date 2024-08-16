class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        List<Integer> ret = new ArrayList<>();
        for(int i=0;i<nums.length;i++){
            int k= Math.abs(nums[i])-1;
            if(nums[k]<0){
                ret.add(k+1);
            }else{
                nums[k]*=-1;
            }
        }
        return ret;
    }
}