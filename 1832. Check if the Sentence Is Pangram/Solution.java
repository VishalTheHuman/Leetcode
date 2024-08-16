class Solution {
    public boolean checkIfPangram(String sentence) {
        if(sentence.length()<26){
            return false;
        }
        int[] arr = new int[26];
        int i =0;
        for(i =0;i<sentence.length();i++){
            arr[sentence.charAt(i)-'a']+=1;
        }
        for(i=0;i<26;i++){
            if(arr[i]==0){
                return false;
            }
        }
        return true;
    }
}