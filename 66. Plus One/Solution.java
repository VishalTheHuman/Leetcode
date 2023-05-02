class Solution {
    public int[] plusOne(int[] digits) {
        int carry = 0;
        if(digits[digits.length-1]+1>9){
            digits[digits.length-1] = (digits[digits.length-1]+1)%10;
            carry=1;
        }else{
            digits[digits.length-1]+=1;
            return digits;
        }
        for(int i = digits.length-2;i>=0;i--){
            if(digits[i]+carry>9){
                digits[i] = (digits[i]+carry)%10;
                carry =1;
            }else{
                digits[i]+=carry;
                return digits;
            }
        }
        int[] digits1 = new int[digits.length+1];
        digits1[0]=carry;
        for(int i = digits.length;i>0;i--){
            digits1[i]=digits[i-1];
        }
        return digits1;
    }
}