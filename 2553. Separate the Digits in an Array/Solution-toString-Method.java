class Solution {
    public int[] separateDigits(int[] nums) {
        StringBuilder ret = new StringBuilder();
        int i = 0;
        for(i=0;i<nums.length;i++){
            ret.append(Integer.toString(nums[i]));
        }
        int[] num = new int[ret.length()];
        for(i=0;i<ret.length();i++){
            num[i]=ret.charAt(i)-'0';
        }
        return num;
    }
}