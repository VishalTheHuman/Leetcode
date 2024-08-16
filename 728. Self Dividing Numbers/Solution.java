class Solution {
    public List<Integer> selfDividingNumbers(int left, int right) {
        int flag=0;
        List<Integer> ret = new ArrayList<>();
        for(int i=left;i<=right;i++){
            flag=0;
            int num =i;
            while(num>0){
                flag=0;
                int mod = num % 10;
                if(mod==0){
                    break;
                }else if((i%mod)==0){
                    flag =1;
                }
                if(flag==0){
                    break;
                }
                num/=10;
            }
            if(flag==1){
                ret.add(i);
            }
        }
        return ret;
    }
}