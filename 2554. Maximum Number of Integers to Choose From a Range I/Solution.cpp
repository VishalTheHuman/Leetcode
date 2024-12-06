class Solution {
public:
    int maxCount(vector<int>& banned, int n, int maxSum) {
        unordered_set store(banned.begin(), banned.end()); 
        int currentSum = 0, count = 0;
        for(int i = 1; i <= n; i++){
            if(store.count(i)!=0){
                continue; 
            }
            if ((currentSum + i) > maxSum) break;
            currentSum+=i; 
            count++;
        }
        return count; 
    }
};
