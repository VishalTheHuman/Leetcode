class Solution {
    public String removeDuplicates(String s) {
        List<Character> ret = new ArrayList<>();
        for(int i = 0;i<s.length();i++){
            if(ret.size()==0){
                ret.add(s.charAt(i));
            }else if(ret.get(ret.size()-1)!=s.charAt(i)){
                ret.add(s.charAt(i));
            }else{
                ret.remove(ret.size()-1);
            }
        }
        String out = "";
        for(int i =0;i<ret.size();i++){
            out+=ret.get(i);
        }
        return out;
    }
}