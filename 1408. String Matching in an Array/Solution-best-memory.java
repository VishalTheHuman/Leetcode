class Solution {
    public List<String> stringMatching(String[] words) {
        List<String> ret = new ArrayList();
        for(String x:words){
            for(String y:words){
                if(!x.equals(y)){
                    if(x.indexOf(y)!=-1 && !ret.contains(y)){
                        ret.add(y);
                    }
                }
            }
        }
        return ret;
    }
}