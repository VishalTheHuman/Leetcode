class Solution {
    public String repeatLimitedString(String s, int repeatLimit) {
        int[] arr = new int[26];
        StringBuilder answer = new StringBuilder(); 
        for(char x : s.toCharArray()){
            arr[x-'a'] += 1; 
        }
        int p1 = 25;  
        while (p1>=0){
            while(p1>=0 && arr[p1]==0){
                p1--;
            } 
            if (p1==-1) break;
            int val = Math.min(repeatLimit, arr[p1]);
            for(int i=0; i<val;i++) {
                answer.append((char)('a' + p1));
            }
            arr[p1]-=val;
            if (arr[p1] == 0) {
                continue; 
            }
            int p2 = p1-1;
            while(p2>=0 && arr[p2]==0) {
                p2--; 
            }
            if (p2==-1) {
                break; 
            }
            answer.append((char)('a' + p2)); 
            arr[p2]--; 
        }
        return answer.toString(); 
    }
}
