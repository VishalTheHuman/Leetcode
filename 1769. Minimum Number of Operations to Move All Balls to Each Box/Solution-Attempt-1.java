class Solution {
    public int[] minOperations(String boxes) {
        int[] ret = new int[boxes.length()];
        for(int i =0;i<boxes.length();i++){
            int tes=0;
            for(int j=0;j<boxes.length();j++){
                if(boxes.charAt(j)=='1'){
                    tes+=(int)Math.abs(i-j);
                }
            }
            ret[i]=tes;
        }
        return ret;
    }
}