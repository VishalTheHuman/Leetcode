class Solution {
    public boolean isValid(String s) {
        Stack<Character> ret = new Stack<>();
        if(s.length()%2!=0){
            return false;
        }
        for(int i=0;i<s.length();i++){
            if(s.charAt(i)=='('|| s.charAt(i)=='{'|| s.charAt(i)=='['){
                ret.push(s.charAt(i));
            }else if(s.charAt(i)==')'){
                if(!ret.empty()){
                    if(ret.peek()=='('){
                        ret.pop();
                    }else{
                        return false;
                    }
                }
                else{
                    return false;
                }
            }else if(s.charAt(i)=='}'){
                if(!ret.empty()){
                    if(ret.peek()=='{'){
                        ret.pop();
                    }else{
                        return false;
                    }
                }
                else{
                    return false;
                }
            }else if(s.charAt(i)==']'){
                if(!ret.empty()){
                    if(ret.peek()=='['){
                        ret.pop();
                    }else{
                        return false;
                    }
                }
                else{
                    return false;
                }
            }
        }
        if(ret.empty()){
            return true;
        }else{
            return false;
        }
    }
}