class Solution {
    public int reverse(int x) {
        if(x>2147483647 ){
            return 0;
        }
        int y=x;
        int sum=0;
        long sum1=0;
        int modulo;
        int flag =0;
        if(x<0){
            flag =1;
            y=y/-1;
        }
        while(y>0){
            modulo=y%10;
            sum=sum*10 + modulo;
            sum1=sum1*10+modulo;
            if(sum1>2147483647){
            return 0;}
            y=y/10;
        }
        sum = (int) sum;
        if(flag==1){
            return -1*((int)sum);
        }
        return (int)sum;
    }
}