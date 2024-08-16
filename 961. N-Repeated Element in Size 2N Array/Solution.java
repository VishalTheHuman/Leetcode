class Solution {
    public int repeatedNTimes(int[] nums) {
        List<Integer> list = new ArrayList<>();
        for(int i:nums){
            if(list.contains(i)){
                return i;
            }
            list.add(i);
        }
        return -1;
    }
}