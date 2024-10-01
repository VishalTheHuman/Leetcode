class Solution {
    public long maximumTotalSum(int[] maximumHeight) {
        long sum = 0; 
        Arrays.sort(maximumHeight);
        long currMax = 1000000000; 
        for(int i = maximumHeight.length - 1; i >= 0; i--){
            currMax = Math.min(currMax, maximumHeight[i]);
            if (currMax == 0){
                return -1;
            }
            sum += currMax;
            currMax -= 1;
        }
        return sum;
    }
}
