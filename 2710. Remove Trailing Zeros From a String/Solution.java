class Solution {
    public String removeTrailingZeros(String num) {
        int size = num.length();
        boolean flag = false;
        while(flag!=true && size>=0){
            size-=1;
            if(num.charAt(size)!='0'){
                flag = true;
            }
        }
        return num.substring(0,size+1);
    }
}