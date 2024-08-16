class Solution {
    public int isPrefixOfWord(String sentence, String searchWord) {
        int count = 1;
        for(String x : sentence.split(" ")){
            if(x.indexOf(searchWord)==0){
                return count;
            }
            count+=1;
        }
        return -1;
    }
}