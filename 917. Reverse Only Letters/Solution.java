class Solution {
    public String reverseOnlyLetters(String s) {
        int i =0;
        int j = s.length()-1;
        char[] ret = s.toCharArray();
        while(j>=i){
            if(isChar(ret[i])){
                if(isChar(ret[j])){
                    char temp = ret[i];
                    ret[i]=ret[j];
                    ret[j]=temp;
                }else{
                    j--;
                    continue;
                }
            }else{
                i++;
                continue;
            }
            i++;
            j--;
        }
        StringBuilder out = new StringBuilder();
        for(int k =0;k<s.length();k++){
            out.append(ret[k]);
        }
        return out.toString();
    }
    public boolean isChar(char ch){
        if((ch>='a' && ch<='z')||(ch>='A' && ch<='Z')){
            return true;
        }
        return false;
    }
}