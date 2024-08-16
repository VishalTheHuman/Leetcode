class Solution {
    public String reversePrefix(String word, char ch) {
        int i = 0;
        while (i < word.length() && word.charAt(i) != ch) {
            i += 1;
        }
        if(i>word.length()){
            return word;
        }
        int j = i;
        String r = "";
        while (j >= 0) {
            r += word.charAt(j);
            j--;
        }
        return r + word.substring(i, word.length());
    }
}