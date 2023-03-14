public class Base7 {
    public static void main(String[] args) {
        System.out.println(convertToBase7(120));
    }
    static String convertToBase7(int num) {
        int sum=0;
        int a;
        int modulo;
        while (num>0){
            modulo= num%7;
            sum=sum*10 + modulo;
            num=(int) num/7;
        }
        String ab = sum.valueOf(sum);
        return sum.toString(sum);
    }
}