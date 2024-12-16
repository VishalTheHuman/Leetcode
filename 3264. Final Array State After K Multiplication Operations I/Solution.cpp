class Solution {
public:
    vector<int> getFinalState(vector<int>& nums, int k, int multiplier) {
        for(int i=0;i<k;i++){
            int idx = -1, val = INT_MAX; 
            for(int j=0;j<nums.size();j++){
                if (nums[j] < val){
                    val = nums[j]; 
                    idx = j;
                }
            }
            nums[idx]*=multiplier; 
        }
        return nums; 
    }
};
