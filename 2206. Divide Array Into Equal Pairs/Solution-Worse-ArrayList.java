class Solution {
    public boolean divideArray(int[] nums) {
        List<Integer> Key = new ArrayList<>();
        List<Integer> Value = new ArrayList<>();
        for(int i =0;i<nums.length;i++){
            if(Key.indexOf(nums[i])==-1){
                Key.add(nums[i]);
                Value.add(1);
            }else{
                Value.set(Key.indexOf(nums[i]),Value.get(Key.indexOf(nums[i]))+1);
            }
        }
        for(int i =0;i<Value.size();i++){
            if(Value.get(i)%2!=0){
                return false;
            }
        }
        return true;
    }
}