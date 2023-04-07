class Solution {
    public int countDigits(int num) {
        int flag = num;
        int count = 0;
        while(flag>0){
            int modulo = flag%10;
            flag/=10;
            if(num%modulo==0){
                count++;
            }
        }
        return count;
    }
}