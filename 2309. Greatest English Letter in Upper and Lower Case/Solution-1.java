class Solution {
    public String greatestLetter(String s) {
        int[] upper = new int[26];
        int[] lower = new int[26];
        for(int i=0;i<s.length();i++){
            if(Character.isUpperCase(s.charAt(i))){
                upper[s.charAt(i)-'A']+=1;
            }else{
                lower[s.charAt(i)-'a']+=1;
            }
        }
        for(int i=25;i>=0;i--){
            if(upper[i]>0 && lower[i]>0){
                return Character.toString((char)'A'+i);
            }
        }
        return "";
    }
}