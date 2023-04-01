import java.util.Arrays;

public class PlusOne{
    public static void main(String[] args){
        Solution one = new Solution();
        int[] news = new int[]{9,8,7,6,5,4,3,2,1,0};
        System.out.println(Arrays.toString(one.plusOne(news)));
    }
    static class Solution {
        public int[] plusOne(int[] digits) {
            long sum=0;
            for(int i=0;i<digits.length;i++){
                sum= sum*10+digits[i];
            }
            sum+=1;
            int length = (int) Math.log(sum)+1;
            int[] Array = new int[length];
            for(int i = length-1;i>=0;i--){
                Array[i]=(int)(sum%10);
                sum=sum/10;
            }
            return Array;
        }
    }
}
