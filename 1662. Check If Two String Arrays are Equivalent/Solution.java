class Solution {
    public boolean arrayStringsAreEqual(String[] word1, String[] word2) {
        for(int i=1;i<word1.length;i++){
            word1[0]+=word1[i];
        }
        for(int i=1;i<word2.length;i++){
            word2[0]+=word2[i];
        }
        if(word1[0].equals(word2[0])){
            return true;
        }
        return false;
    }
}