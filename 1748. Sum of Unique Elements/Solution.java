class Solution {
    public int sumOfUnique(int[] nums) {
        HashMap<Integer, Integer> ret = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (ret.get(nums[i]) == null) {
                ret.put(nums[i], 1);
            } else {
                ret.put(nums[i], ret.get(nums[i]) + 1);
            }
        }
        int sum = 0;
        for (Map.Entry<Integer, Integer> entry : ret.entrySet()) {
            if (entry.getValue() == 1) {
                sum += entry.getKey();
            }
        }
        return sum;
    }
}
