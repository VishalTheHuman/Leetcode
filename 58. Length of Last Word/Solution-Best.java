class Solution {
    public int lengthOfLastWord(String s) {
        s = s.strip();
        int count = 0;
        int i = s.length()-1;
        while(i>=0){
            if(s.charAt(i)!=' '){
                count+=1;
                i-=1;
                continue;
            }
            return count;
        }
        return count;
    }
}