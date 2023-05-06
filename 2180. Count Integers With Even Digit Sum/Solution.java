class Solution {
    public int countEven(int num) {
        int count = 0;
        for(int i=2;i<=num;i++){
            int tes = i;
            int sum =0;
            while(tes>0){
                sum += tes%10;
                tes/=10;
            }
            if(sum%2==0){
                count++;
            }
        }
        return count;
    }
}