class Solution {
    public List<String> cellsInRange(String s) {
        List<String> ret = new ArrayList<>();
        for(char ch = s.charAt(0);ch<=s.charAt(3);ch++){
            for(char ch1 = s.charAt(1);ch1<=s.charAt(4);ch1++){
                ret.add(""+ch+ch1);
            }
        }
        return ret;
    }
}