class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        HashMap<Integer,Integer> table = new HashMap<>();
        List<Integer> ret = new ArrayList<>();
        for(int i=0;i<nums.length;i++){
            if(table.get(nums[i])==null){
                table.put(nums[i],1);
            }else{
                ret.add(nums[i]);
            }
        }
        return ret;
    }
}