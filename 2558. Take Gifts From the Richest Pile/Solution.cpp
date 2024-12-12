class Solution {
public:
    long long pickGifts(vector<int>& gifts, int k) {
        long long answer = 0; 
        priority_queue<int> q; 
        for(int x : gifts) q.push(x);
        for(int i=1;i<=k;i++){
            int val = q.top();
            if (val<=1) break; 
            q.pop();
            q.push(sqrt(val));
        }
        while (!q.empty()){
            answer += q.top();
            q.pop();
        }
        return answer; 
    }
};
