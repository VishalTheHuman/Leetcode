class Solution {
    public void rotate(int[] nums, int k) {
        k=k% nums.length;
        int i;
        int[] store = new int[k];
        for(i= nums.length-1;i> nums.length-1-k;i--){
            store[nums.length-i-1]=nums[i];
        }
        for(i= nums.length-1-k;i>=0;i--){
            nums[i+k]=nums[i];
        }
        for(i=0;i<store.length;i++){
            nums[i]=store[store.length-1-i];
        }
        return;
    }
}