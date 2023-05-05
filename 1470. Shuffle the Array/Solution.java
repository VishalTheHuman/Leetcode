class Solution {
    public int[] shuffle(int[] nums, int n) {
        int i=0;
        int j=n;
        int k=0;
        int[] tes = new int[2*n];
        while(k<2*n){
            tes[k]=nums[i];
            k++;
            tes[k]=nums[j];
            k++;
            i++;
            j++;
        }
        return tes;
    }
}