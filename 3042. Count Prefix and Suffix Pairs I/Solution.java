class Solution {
    public int countPrefixSuffixPairs(String[] words) {
        int count = 0; 
        for(int i=0;i<words.length;i++){
            for(int j=i+1;j<words.length;j++){
                if (i==j) continue; 
                if (isPrefixAndSuffix(words[i], words[j])){
                    count++;
                }
            }
        }
        return count; 
    }

    public boolean isPrefixAndSuffix(String str1, String str2){
        int str1length = str1.length();
        int str2length = str2.length();
        
        if (str1length > str2length) {
            return false; 
        }
        int diff = str2length - str1length;
        for(int i=0; i<str1length;i++) {
            if ((str1.charAt(i)!=str2.charAt(i)) 
            || (str1.charAt(i)!=str2.charAt(diff+i))) {
                return false; 
            }
        }
        return true; 
    }
}
