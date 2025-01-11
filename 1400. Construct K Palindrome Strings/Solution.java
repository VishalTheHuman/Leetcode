class Solution {
    public boolean canConstruct(String s, int k) {
        if (s.length() < k) return false;
        Map<Character, Integer> store = new HashMap<>(); 
        for(char ch : s.toCharArray()){
            store.put(ch, store.getOrDefault(ch,0) + 1); 
        }
        int oddChars = 0; 
        for(Integer value : store.values()){
            if (value%2==1){
                oddChars++;
            }
        }
        return (oddChars <= k) ; 
    }
}
