class Solution {
    public int maxDepth(String s) {
        Stack<Character> ret = new Stack<>();
        int large = 0;
        for(int i=0;i<s.length();i++){
            if(s.charAt(i)=='('){
                ret.push('(');
            }else if(s.charAt(i)==')'){
                ret.pop();
            }
            if(ret.size()>large){
                large = ret.size();
            }
        }
        return large;
    }
}