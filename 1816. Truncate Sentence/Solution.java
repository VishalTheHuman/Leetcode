class Solution {
    public String truncateSentence(String s, int k) {
        int track=0;
        int index =s.length();
        for(int i=0;i<s.length();i++){
            if(s.charAt(i)==' '){
                if(track==k-1){
                    index = i;
                    break;
                }
                track++;
            }
        }
        return s.substring(0,index);
    }
}