class Solution {
    public int[] replaceElements(int[] arr) {
        int large = arr[arr.length-1];
        for(int i=arr.length-2;i>=0;i--){
            int temp = arr[i];
            arr[i]=large;
            if(temp>large){
                large = temp;
            }
        }
        arr[arr.length-1]=-1;
        return arr;
    }
}