class Solution {
    public void moveZeroes(int[] nums) {
        List<Integer> ret = new ArrayList<>();
        for(int i =0;i<nums.length;i++){
            if(nums[i]!=0){
                ret.add(nums[i]);
            }
        }
        for(int i =0;i<ret.size();i++){
            nums[i]=ret.get(i);
        }
        for(int i =ret.size();i<nums.length;i++){
            nums[i]=0;
        }
    }
}