class Solution {
public:
    bool canChange(string start, string target) {
        int i = 0, j = 0; 
        int length = target.size();
        while (j < length){
            if(target[j]=='L'){
                while(i < length && start[i]=='_'){
                    i++;
                }
                if(i==length || i<j || start[i]!='L') return false;
                i++;
            }else if (target[j]=='R'){
                if (i>j) return false;
                while(i <= j && start[i]=='_'){
                    i++;
                }
                if(i>j || start[i]!='R') return false;
                i++;
            }
            j++;
        }
        while(i < length && start[i]=='_'){
            i++;
        }
        return i==length; 
    }
};
