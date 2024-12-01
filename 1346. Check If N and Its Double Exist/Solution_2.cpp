class Solution {
public:
    bool checkIfExist(vector<int>& arr) {
        unordered_set<int> store; 
        for(int i=0;i<arr.size();i++){
            if (arr[i]%2==0){
                if (store.find(arr[i]/2) != store.end()){
                    return true; 
                }
            }
            
            if (store.find(arr[i]*2) != store.end()){
                return true;
            }
            
            store.insert(arr[i]);
        }
        return false; 
    }
};
