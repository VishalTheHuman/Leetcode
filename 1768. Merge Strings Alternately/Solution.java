class Solution {
    public String mergeAlternately(String word1, String word2) {
        StringBuilder ret = new StringBuilder();
        int max;
        if(word1.length()>=word2.length()){
            max = word1.length();
        }else{
            max = word2.length();
        }
        int i = 0;
        int j = 0;
        while(i<max && j<max){
            if(i<word1.length()){
                ret.append(word1.charAt(i));
                i++;
            }
            if(j<word2.length()){
                ret.append(word2.charAt(j));
                j++;
            }
        }
        return ret.toString();
    }
}