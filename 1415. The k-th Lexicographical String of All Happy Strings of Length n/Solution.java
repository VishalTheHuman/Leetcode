class Solution {
    int count = 0, kth; 
    boolean found = false; 
    char[] arr = new char[]{'a','b','c'}; 
    Stack<Character> store = new Stack<>(); 
    public String getHappyString(int n, int k) {
        kth = k;
        traverse(n, 'd');
        if (found){
            StringBuilder result = new StringBuilder();
            for(int i=store.size()-1;i>=0;i--){
                result.append(store.get(i)); 
            }
            return result.toString(); 
        }
        return "";
    }

    public void traverse(int n, char prev){
        if (found) return; 
        if (n==0){
            count++; 
            if (count == kth){
                found = true; 
            }
            return; 
        }
        for(char x : arr){
            if (x !=prev){
                traverse(n-1, x); 
                store.push(x); 
                if (found) break; 
                store.pop();
            }
        }
    }
}
