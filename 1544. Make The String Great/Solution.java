class Solution {
    public String makeGood(String s) {
        StringBuilder ret = new StringBuilder();
        Stack<Character> st = new Stack<>();
        for(int i=0;i<s.length();i++){
            if(!st.empty()){
                if(isUpper(s.charAt(i))){
                    if(st.peek()==Character.toLowerCase(s.charAt(i))) st.pop();
                    else st.push(s.charAt(i));
                }else if(isLower(s.charAt(i))){
                    if(st.peek()==Character.toUpperCase(s.charAt(i))) st.pop();
                    else st.push(s.charAt(i));
                }
                else{
                    st.push(s.charAt(i));
                }
            }else{
                st.push(s.charAt(i));
            }
        }
        while(!st.empty()){
            ret.insert(0,st.pop());
        }
        return ret.toString();
    }
    public boolean isUpper(char ch){
        if(ch>='A'&& ch<='Z'){
            return true;
        }
        return false;
    }
    public boolean isLower(char ch){
        if(ch>='a'&& ch<='z'){
            return true;
        }
        return false;
    }
}