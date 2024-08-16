class Solution {
    public String greatestLetter(String s) {
        for(char i ='Z';i>='A';i--){
            if(s.indexOf(Character.toLowerCase(i))!=-1 && s.indexOf(i)!=-1){
                return Character.toString(i);
            }
        }
        return "";
    }
}