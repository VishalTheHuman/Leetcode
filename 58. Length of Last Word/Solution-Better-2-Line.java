class Solution {
    public int lengthOfLastWord(String s) {
        String[] ret = s.strip().split(" ");
        return ret[ret.length-1].length();
    }
}