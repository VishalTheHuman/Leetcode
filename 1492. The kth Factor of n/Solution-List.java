class Solution {
    public int kthFactor(int n, int k) {
        List<Integer> ret = new ArrayList<>();
        for(int i = 1;i<=n;i++){
            if(ret.size()==k) return ret.get(ret.size()-1);
            if(n%i==0) ret.add(i);
        }
        if(ret.size()==k){
            return n;
        }
        return -1;
    }
}