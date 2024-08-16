class Solution {
    public boolean divideArray(int[] nums) {
        HashMap<Integer,Integer> tab = new HashMap<>();
        for(int i=0;i<nums.length;i++){
            if(tab.get(nums[i])==null){
                tab.put(nums[i],1);
            }else{
                tab.put(nums[i],tab.get(nums[i])+1);
            }
        }
        for(Map.Entry<Integer,Integer> x:tab.entrySet()){
            if(x.getValue()%2!=0){
                return false;
            }
        }
        return true;
    }
}