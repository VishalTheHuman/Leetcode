class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        for(int i=0; i < grid.size(); i++){
            for(int j=0; j<grid[i].size(); j++){
                int val = INT_MAX;
                if ((i-1) >= 0) val = grid[i-1][j];
                if ((j-1) >=0) val = min(val, grid[i][j-1]);
                if (val==INT_MAX) continue;
                grid[i][j] += val;
            }
        }
        return grid[grid.size()-1][grid[0].size()-1];
    }
};
