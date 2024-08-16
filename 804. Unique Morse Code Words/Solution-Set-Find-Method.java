class Solution {
    public int uniqueMorseRepresentations(String[] words) {
        String[] MorseEquivalent = new String[]{".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};
        int j =0;
        StringBuilder ret = new StringBuilder();
        for(String x : words){
            ret.setLength(0);
            for(int i =0;i<x.length();i++){
                ret.append(MorseEquivalent[x.charAt(i)-'a']);
            }
            words[j]=ret.toString();
            j+=1;
        }
        j=1;
        Arrays.sort(words);
        for(int i=0;i<words.length-1;i++){
            if(!words[i].equals(words[i+1])) j+=1;
        }
        return j;
    }
}