class Solution {
    public String replaceDigits(String s) {
        String ret = "";
        for(int i=0;i<s.length();i++){
            if(i%2==1){
                char temp = (char)(s.charAt(i-1)+intparse(s.charAt(i)));
                ret+=temp;
            }else{
                ret+=s.charAt(i);
            }
        }
        return ret;
    }
    public int intparse(char ch){
        int temp = ch-48;
        return temp;
    }
}