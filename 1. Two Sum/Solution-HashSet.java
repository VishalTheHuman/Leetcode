class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer,Integer> dict = new HashMap<>();
        for(int i=0;i<nums.length;i++){
            if(dict.get(nums[i])==null){
                dict.put(nums[i],i);
            }
        }
        for(int i=0;i<nums.length;i++){
            if(dict.get(target-nums[i])!=null){
                if(dict.get(target-nums[i])!=i){
                    return new int[]{i,dict.get(target-nums[i])};
                }
            }
        }
        return new int[]{-1,-1};
    }
}