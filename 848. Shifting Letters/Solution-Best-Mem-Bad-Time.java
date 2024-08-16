class Solution {
    public String shiftingLetters(String s, int[] shifts) {
        StringBuilder str = new StringBuilder(s);
        int sum =0;
        for(int j=shifts.length-1;j>=0;j--){
            sum+=shifts[j];
            sum%=26;
            if(sum+(int)str.charAt(j)<123){
                char temp = (char) (str.charAt(j)+sum);
                str.deleteCharAt(j);
                str.insert(j,temp);
            }else{
                char temp = (char)(((str.charAt(j)+sum)%123) + 'a');
                str.deleteCharAt(j);
                str.insert(j,temp);
            }
        }
        String ret = str.toString();
        return ret;
    }
}