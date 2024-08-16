class Solution {
    public boolean isSameAfterReversals(int num) {
        int temp = num;
        int num1 = 0;
        while(temp>0){
            num1 = num1*10 + (temp%10);
            temp/=10;
        }
        temp = 0;
        while(num1>0){
            temp = temp*10 + (num1%10);
            num1/=10;
        }
        if(temp==num){
            return true;
        }
        return false;
    }
}