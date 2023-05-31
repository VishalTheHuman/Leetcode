class Solution {
    public boolean isValid(String s) {
        List<Character> ret = new ArrayList<>();
        if(s.length()%2!=0){
            return false;
        }
        for(int i=0;i<s.length();i++){
            if(s.charAt(i)=='('|| s.charAt(i)=='{'|| s.charAt(i)=='['){
                ret.add(s.charAt(i));
            }else if(s.charAt(i)==')'){
                if(ret.size()>0){
                    if(ret.get(ret.size()-1)=='('){
                        ret.remove(ret.size()-1);
                    }else{
                        return false;
                    }
                }
                else{
                    return false;
                }
            }else if(s.charAt(i)=='}'){
                if(ret.size()>0){
                    if(ret.get(ret.size()-1)=='{'){
                        ret.remove(ret.size()-1);
                    }else{
                        return false;
                    }
                }
                else{
                    return false;
                }
            }else if(s.charAt(i)==']'){
                if(ret.size()>0){
                    if(ret.get(ret.size()-1)=='['){
                        ret.remove(ret.size()-1);
                    }else{
                        return false;
                    }
                }
                else{
                    return false;
                }
            }
        }
        if(ret.size()==0){
            return true;
        }else{
            return false;
        }
    }
}