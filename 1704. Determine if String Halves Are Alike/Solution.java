class Solution {
    public boolean halvesAreAlike(String s) {
        String half1 = s.substring(0,s.length()/2).toLowerCase();
        s = s.substring(s.length()/2).toLowerCase();
        int vow1=0,vow2=0;
        for(int i=0;i<s.length();i++){
            if(half1.charAt(i)=='a'||half1.charAt(i)=='e'||half1.charAt(i)=='i'||half1.charAt(i)=='o'||half1.charAt(i)=='u'){
                vow1++;
            }
            if(s.charAt(i)=='a'||s.charAt(i)=='e'||s.charAt(i)=='i'||s.charAt(i)=='o'||s.charAt(i)=='u'){
                vow2++;
            }
        }
        if(vow1==vow2){
            return true;
        }
        return false;
    }
}