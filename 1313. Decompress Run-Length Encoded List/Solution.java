class Solution {
    public int[] decompressRLElist(int[] nums) {
        List<Integer> ret = new ArrayList<>();
        for(int i=0;i<nums.length;i+=2){
            int freq=nums[i];
            int val =nums[i+1];
            for(int j=0;j<freq;j++){
                ret.add(val);
            }
        }
        int[] out = new int[ret.size()];
        for(int i=0;i<ret.size();i++){
            out[i]=ret.get(i);
        }
        return out;
    }
}