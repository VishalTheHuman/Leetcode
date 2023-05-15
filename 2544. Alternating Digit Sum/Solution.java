class Solution {
    public int alternateDigitSum(int n) {
        int flag;
        if(((int)Math.log10(n)+1)%2==1){
            flag = 1;
        }else{
            flag = 0;
        }
        int sum = 0;
        while(n>0){
            if(flag%2==0){
                sum += -1*(n%10);
                flag++;
            }else{
                sum += (n%10);
                flag++;
            }
            n/=10;
        }
        return sum;
    }
}