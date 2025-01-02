class Solution {
    public int minOperations(int[] nums, int k) {
        HashMap<Integer, Boolean> store = new HashMap<>();
        for(int x : nums){
            if (x<k) return -1; 
            if (!store.containsKey(x)){
                store.put(x, true);
            }
        }
        return store.size() - (store.containsKey(k) ? 1 : 0);
    }
}
