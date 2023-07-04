class Solution {
    public int numOfPairs(String[] nums, String target) {
        StringBuilder ret = new StringBuilder();
        int count = 0;
        for(int i=0;i<nums.length;i++){
            for(int j=0;j<nums.length;j++){
                if(i!=j){
                    ret.append(nums[i]);
                    ret.append(nums[j]);
                    if(target.equals(ret.toString())){
                        count+=1;
                    }
                    ret.setLength(0);
                }
            }
        }
        return count;
    }
}