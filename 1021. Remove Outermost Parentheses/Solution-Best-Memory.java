class Solution {
    public String removeOuterParentheses(String s) {
        StringBuilder ret = new StringBuilder();
        Stack<Character> out = new Stack<>();
        for(int i =0;i<s.length();i++){
            if(out.size()==1 && s.charAt(i)==')'){
                out.pop();
            }else if(out.empty()){
                out.push(s.charAt(i));
            }else{
                if(s.charAt(i)=='('){
                    out.push('(');
                    ret.append('(');
                }else{
                    out.pop();
                    ret.append(')');
                }
            }
        }
        return ret.toString();
    }
}