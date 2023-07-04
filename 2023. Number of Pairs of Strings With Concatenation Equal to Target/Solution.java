class Solution {
    public int numOfPairs(String[] nums, String target) {
        int count = 0;
        for(int i=0;i<nums.length;i++){
            for(int j=0;j<nums.length;j++){
                if(i!=j){
                    String ret = nums[i]+nums[j];
                    if(target.equals(ret)){
                        count+=1;
                    }
                }
            }
        }
        return count;
    }
}