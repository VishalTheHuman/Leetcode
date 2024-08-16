class Solution {
    public boolean backspaceCompare(String s, String t) {
        StringBuilder ret1 = new StringBuilder();
        StringBuilder ret2 = new StringBuilder();
        for(int i =0;i<s.length();i++){
            if(s.charAt(i)=='#'){
                if(ret1.length()!=0){
                    ret1.deleteCharAt(ret1.length()-1);
                }
            }else{
                ret1.append(s.charAt(i));
            }
        }
        for(int i =0;i<t.length();i++){
            if(t.charAt(i)=='#'){
                if(ret2.length()!=0){
                    ret2.deleteCharAt(ret2.length()-1);
                } 
            }else{
                ret2.append(t.charAt(i));
            }
        }
        if(ret1.toString().equals(ret2.toString())){
            return true;
        }
        return false;
    }
}