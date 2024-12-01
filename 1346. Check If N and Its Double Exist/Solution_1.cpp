class Solution {
public:
    bool checkIfExist(vector<int>& arr) {
        unordered_set<int> store; 
        for(int i=0;i<arr.size();i++){
            for(int j=0;j<arr.size();j++){
                if (i!=j && (arr[i]*2 == arr[j] || arr[i] == arr[j]*2)){
                    return true; 
                }
            }
        }
        return false; 
    }
};
