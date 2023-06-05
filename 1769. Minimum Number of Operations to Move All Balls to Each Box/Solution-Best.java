class Solution {
    public int[] minOperations(String boxes) {
        char[] arr = boxes.toCharArray();
        int len = boxes.length();
        int[] left = new int[len];
        int[] right = new int[len];
        int i=0;
        int countL=0,countR=0,distanceL=0,distanceR=0;
        for(i=0;i<len;i++){
            distanceL+=countL;
            left[i]=distanceL;
            countL +=(arr[i]-'0');
            distanceR+=countR;
            right[len-1-i]=distanceR;
            countR +=(arr[len-1-i]-'0');
        }
        for(i=0;i<len;i++){
            left[i]+=right[i];
        }
        return left;
    }
}