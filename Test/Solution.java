public class Solution {
    public static int finalValueAfterOperations(String[] operations) {
        int x =0;
        for(String y:operations){
            System.out.println(y);
            if(y=="++X" || y=="X++"){
                x++;
            }else{
                x--;
            }
        }
        return x;
    }
    public static void main(String[] args) {
        String[] tst = {"++X","++X","X++"};
        finalValueAfterOperations(tst);
    }
}