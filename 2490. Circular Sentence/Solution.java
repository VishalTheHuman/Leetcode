class Solution {
    public boolean isCircularSentence(String sentence) {
        String[] ret = sentence.split(" ");
        for(int i =0;i<ret.length;i++){
            if(ret[i].charAt(ret[i].length()-1)!=ret[(i+1)%ret.length].charAt(0)){
                return false;
            }
        }
        return true;
    }
}