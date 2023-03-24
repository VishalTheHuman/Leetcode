public class Solution {
    public static void main(String[] args) {
        System.out.println(evenOddBit(2));
    }
    static int[] evenOddBit(int n) {
        String binaryString = Integer.toBinaryString(n);
        System.out.println(binaryString);
        int a = binaryString.length();
        int even=0; odd =0;
        for(int i=a;i>0;i--){
            if(binaryString.charAt(a-1-i)=='1' && (a-1-i)%2==0){
                even++;
            }else if (binaryString.charAt(a-1-i)=='1' && (a-1-i)%2==){
                odd++;
            }
    }
}