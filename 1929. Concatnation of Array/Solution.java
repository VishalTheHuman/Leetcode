class Solution {
    public int[] getConcatenation(int[] nums) {
        int[] array = new int[2*nums.length];
        for(int i=0;i<nums.length;i++)
        {
            array[i]=nums[i];
            array[nums.length+i]=nums[i];
        }
        return array;
    }
}