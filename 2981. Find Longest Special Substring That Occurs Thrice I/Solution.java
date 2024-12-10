class Solution {
    public int maximumLength(String s) {
        Map<String, Integer> store = new HashMap<>(); 
        int length = s.length();
        for(int i=length-2; i>0; i--){
            for(int j=0;j<length-i+1; j++){
                String curr = s.substring(j,j+i);
                if (verify(curr)){
                    store.put(curr, store.getOrDefault(curr, 0)+1); 
                    if(store.get(curr)==3) return i; 
                }
            }
        }
        return -1;
    }

    public boolean verify(String s){
        for(int i=1;i<s.length();i++){
            if (s.charAt(i)!=s.charAt(i-1)) return false; 
        }
        return true; 
    }
}
