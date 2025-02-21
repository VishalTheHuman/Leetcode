class Solution {
    public int minOperations(int[] nums, int k) {
        PriorityQueue<Long> store = new PriorityQueue(); 
        for(int x : nums){
            store.add((long) x);
        }
        int count = 0; 

        while(store.peek()<k){
            long x = store.poll(); 
            long y = store.poll(); 
            store.add(Math.min(x, y) * 2 + Math.max(x, y)); 
            count++;
        }
        return count; 
    }
}
