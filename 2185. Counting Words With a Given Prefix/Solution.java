class Solution {
    public int prefixCount(String[] words, String pref) {
        int count = 0;
        for(String x:words){
            if(x.indexOf(pref)==0){
                count+=1;
            }
        }
        return count;
    }
}