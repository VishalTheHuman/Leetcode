class Solution {
    public List<String> buildArray(int[] target, int n) {
        List<String> ret = new ArrayList<>();
        int ptr = 0;
        int k=1;
        while(ptr<target.length){
            if(target[ptr]==k){
                ret.add("Push");
                ptr+=1;
            }else{
                ret.add("Push");
                ret.add("Pop");
            }
            k+=1;
        }
        return ret;
    }
}