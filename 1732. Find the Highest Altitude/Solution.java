class Solution {
    public int largestAltitude(int[] gain) {
        int[] flag = new int[gain.length+1];
        flag[0]=0;
        int large = flag[0];
        for(int i=1;i<flag.length;i++){
            flag[i]=flag[i-1]+gain[i-1];
            if(flag[i]>large){
                large = flag[i];
            }
        }
        return large;
    }
}