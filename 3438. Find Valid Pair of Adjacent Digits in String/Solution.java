class Solution {  
    public String findValidPair(String s) {  
        HashMap<Character, Integer> store = new HashMap<>();  
        HashSet<Character> seen = new HashSet<>();  
        for(char x : s.toCharArray()){  
            store.put(x, store.getOrDefault(x,0)+1);  
        }  
        for(int i=1;i<s.length();i++){  
            char c1 = s.charAt(i-1);  
            char c2 = s.charAt(i);  
            int s1 = (int) c1 - '0';  
            int s2 = (int) c2 - '0';  
            if (c1!=c2 &&  
            store.get(c2)==s2 &&  
            store.get(c1)==s1) {  
                return new String(new char[]{c1,c2});  
            }  
        }  
        return "";  
    }  
}
