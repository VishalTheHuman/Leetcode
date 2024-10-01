class Solution {
    public boolean canArrange(int[] arr, int k) {
        Map<Integer, Integer> store = new HashMap<>();
        for(int i = 0; i < arr.length; i++){
            arr[i] = ((arr[i] % k) + k) % k;
            store.put(arr[i], store.getOrDefault(arr[i], 0) + 1);
        }
        if (store.containsKey(0)){
            if (store.get(0)%2==1){
                return false;
            }
            store.remove(0);
        }
        for(int x : store.keySet()){
            int val1 = store.getOrDefault(k-x, -1); 
            int val2 = store.getOrDefault(x, -1);
            if (val1 != val2){
                return false;
            }
        }
        return true;
    }
}
