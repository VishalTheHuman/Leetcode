class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        HashMap<Integer,Integer> table = new HashMap<>();
        for(int i=0;i<nums.length;i++){
            if(table.get(nums[i])==null){
                table.put(nums[i],1);
            }else{
                table.put(nums[i],table.get(nums[i])+1);
            }
        }
        List<Integer> ret = new ArrayList<>();
        for(Map.Entry<Integer,Integer> x : table.entrySet()){
            if(x.getValue()>1){
                ret.add(x.getKey());
            }
        }
        return ret;
    }
}