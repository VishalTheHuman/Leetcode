class Solution {
    public boolean squareIsWhite(String coordinates) {
        if((coordinates.charAt(0)+coordinates.charAt(1))%2==0){
            return false;
        }
        return true;
    }
}