class Solution {
    public int minAddToMakeValid(String s) {
        Stack<Character> ret = new Stack<>();
        for(int i =0;i<s.length();i++){
            if(s.charAt(i)=='('){
                ret.push('(');
            }else{
                if(!ret.empty()){
                    if(ret.peek()=='('){
                        ret.pop();
                    }else{
                        ret.push(')');
                    }
                }else{
                    ret.push(')');
                }
                
            }
        }
        return ret.size();
    }
}