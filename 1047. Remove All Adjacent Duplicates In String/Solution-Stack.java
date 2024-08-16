class Solution {
    public String removeDuplicates(String s) {
        Stack<Character> ret = new Stack<Character>();
        for(int i =0;i<s.length();i++){
            if(ret.empty()){
                ret.push(s.charAt(i));
            }else if(ret.peek()!=s.charAt(i)){
                ret.push(s.charAt(i));
            }else{
                ret.pop();
            }
        }
        StringBuilder out = new StringBuilder();
        while(!ret.empty()){
            out.insert(0,ret.pop());
        }
        return out.toString();
    }
}