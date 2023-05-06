class Solution {
    public int sumBase(int n, int k) {
        int base_num =0;
        int mod;
        while(n>0){
            mod = n%k;
            base_num = base_num*10 + mod;
            n/=k;
        }
        int sum = 0;
        while(base_num>0){
            mod=base_num%10;
            base_num/=10;
            sum+=mod;
        }
        return sum;
    }
}