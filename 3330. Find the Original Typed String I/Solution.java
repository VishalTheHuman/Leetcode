class Solution {
    public int possibleStringCount(String word) {
        int count = 0, i=1, prev = -1; 
        while(i<word.length()){
            if(word.charAt(i)==word.charAt(i-1)){
                count++;
                while((i < word.length()) && (word.charAt(i)==word.charAt(i-1))){
                    i++;
                    count++;
                }
                prev++;
                continue;
            }
            i++;
        }
        return Math.max(count - Math.max(prev,0),1);
    }
}
