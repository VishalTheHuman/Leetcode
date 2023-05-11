class Solution {
    public String reverseWords(String s) {
        String[] split = s.split(" ");
        StringBuilder ret = new StringBuilder();
        for(String x : split){
            for(int i = x.length()-1;i>=0;i--){
                ret.append(x.charAt(i));
            }
            ret.append(" ");
        }
        s = ret.toString();
        return s.trim();
    }
}