class Solution {
    public String shiftingLetters(String s, int[] shifts) {
        char[] str = s.toCharArray();
        int sum =0;
        for(int j=shifts.length-1;j>=0;j--){
            sum+=shifts[j];
            sum%=26;
            if(sum+(int)str[j]<123){
                char temp = (char) (str[j]+sum);
                str[j] = temp;
            }else{
                char temp = (char)(((str[j]+sum)%123) + 'a');
                str[j] = temp;
            }
        }
        return new String(str);
    }
}