class Solution {
    public String decodeMessage(String key, String message) {
        List<Character> keys = new ArrayList<>();
        List<Character> value = new ArrayList<>();
        int i = 0;
        int a = 0;
        while (keys.size() < 26) {
            if (keys.contains(key.charAt(i))==false && key.charAt(i)!=' ') {
                value.add((char)('a'+a));
                keys.add(key.charAt(i));
                a+=1;
            }
            i += 1;
        }
        StringBuilder out = new StringBuilder();
        for (i = 0; i < message.length(); i++) {
            if (message.charAt(i) != ' ') {
                out.append(value.get(keys.indexOf(message.charAt(i))));
            } else {
                out.append(' ');
            }
        }
        return out.toString();
    }
}