class Solution {
    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        List<List<Integer>> outer = new ArrayList<>();
        List<Integer> num1 = new ArrayList<>();
        List<Integer> num2 = new ArrayList<>();
        int flag1 =0,flag2 =0;
        for(int i=0;i<nums1.length;i++){
            flag1 =0;
            for(int j=0;j<nums2.length;j++){
                if(nums1[i]==nums2[j]){
                    flag1 = 1;
                }
            }
            if(flag1 != 1 && num1.contains(nums1[i])==false){
                num1.add(nums1[i]);
            }
        }

        for(int i=0;i<nums2.length;i++){
            flag2=0;
            for(int j=0;j<nums1.length;j++){
                if(nums2[i]==nums1[j]){
                    flag2=1;
                }
            }
            if(flag2 != 1 && num2.contains(nums2[i])==false){
                num2.add(nums2[i]);
            }
        }
        outer.add(num1);
        outer.add(num2);
        return outer;
    }
}