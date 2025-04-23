class Solution {
    public int countLargestGroup(int n) {
        HashMap<Integer, Integer> store = new HashMap(); 
        for(int i=1;i<=n;i++){
            int currSum = 0; 
            int num = i; 
            while(num>0){
                currSum += (num%10); 
                num/=10; 
            }
            store.put(currSum, store.getOrDefault(currSum,0)+1); 
        }
        int max = 0; 
        for(Integer x : store.values()){
            max = Math.max(max, x); 
        }
        int count = 0; 
        for(Integer x : store.values()){
            if (x==max) count++;
        }
        return count; 
    }
}
