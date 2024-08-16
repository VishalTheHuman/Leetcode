class Solution {
    public boolean isSumEqual(String firstWord, String secondWord, String targetWord) {
        int fw = 0,sw=0,tw=0;
        for(char c : firstWord.toCharArray()){
            fw = fw*10+(int)(c-97);
        }
        for(char c : secondWord.toCharArray()){
            sw = sw*10+(int)(c-97);
        }
        for(char c:targetWord.toCharArray()){
            tw = tw*10+(int)(c-97);
        }
        if(sw+fw==tw){
            return true;
        }
        return false;
    }
}