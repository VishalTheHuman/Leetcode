class Solution {
    public String replaceDigits(String s) {
        StringBuilder ret = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            if (i % 2 == 1) {
                char temp = (char) (s.charAt(i - 1) - '0' + s.charAt(i));
                ret.append(temp);
            } else {
                ret.append(s.charAt(i));
            }
        }
        String out = ret.toString();
        return out;
    }
}