class Solution {
    public String reverseVowels(String s) {
        int i=0; 
        if(s.length()==1 || s.length()==0){
            return s;
        }
        int j=s.length();
        char[] str = s.toCharArray();
        while(j>i){
            if(isVowel(str[i])){
                while(j>=i){
                    j--;
                    if(isVowel(str[j])){
                        char temp = str[i];
                        str[i]=str[j];
                        str[j]=temp;
                        break;
                    }
                }
            }
            i++;
        }
        return new String(str);
    }
    boolean isVowel(char a){
        if(a=='a'||a=='e'||a=='i'||a=='o'||a=='u'||a=='A'||a=='E'||a=='I'||a=='O'||a=='U'){
            return true;
        }
        return false;
    }
}