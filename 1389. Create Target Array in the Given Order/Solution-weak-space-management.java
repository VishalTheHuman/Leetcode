class Solution {
    public int[] createTargetArray(int[] nums, int[] index) {
        List<Integer> ret = new ArrayList<>();
        for(int i=0;i<nums.length;i++){
            ret.add(index[i],nums[i]);
        }
        int[] out =new int[nums.length];
        for(int i=0;i<nums.length;i++){
            out[i]=ret.get(i);
        }
        return out;
    }
}