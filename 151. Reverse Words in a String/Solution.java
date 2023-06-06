class Solution {
    public String reverseWords(String s) {
        String[] ret = s.trim().split(" ");
        StringBuilder out = new StringBuilder();
        for(int i =ret.length-1;i>=0;i--){
            if(!ret[i].equals("")){
                out.append(ret[i]);
                out.append(" ");
            }
        }
        return out.toString().trim();
    }
}