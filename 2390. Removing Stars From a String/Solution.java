class Solution {
    public String removeStars(String s) {
        List<Character> ret = new ArrayList<>();
        for(int i = 0;i<s.length();i++){
            if(s.charAt(i)=='*'){
                if(ret.size()!=0){
                    ret.remove(ret.size()-1);
                }
            }else{
                ret.add(s.charAt(i));
            }
        }
        StringBuilder out = new StringBuilder();
        for(int i =0;i<ret.size();i++){
            out.append(ret.get(i));
        }
        return out.toString();
    }
}