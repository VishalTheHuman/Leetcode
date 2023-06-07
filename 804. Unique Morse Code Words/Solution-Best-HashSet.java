class Solution {
    public int uniqueMorseRepresentations(String[] words) {
        String[] MorseEquivalent = new String[]{".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};
        HashSet<String> r = new HashSet<>();
        StringBuilder ret = new StringBuilder();
        for(String x : words){
            ret.setLength(0);
            for(int i =0;i<x.length();i++){
                ret.append(MorseEquivalent[x.charAt(i)-'a']);
            }
            r.add(ret.toString());
        }
        return r.size();
    }
}