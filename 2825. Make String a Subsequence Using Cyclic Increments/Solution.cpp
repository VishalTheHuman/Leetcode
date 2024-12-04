class Solution {
public:
    bool canMakeSubsequence(string str1, string str2) {
        if (str1.size() < str2.size()) return false;
        int i = 0, j = 0; // i - str1 ; i - str2 ;
        int s1 = str1.size() , s2 = str2.size();
        while (i < s1 && j < s2){
            if ((str1[i]==str2[j]) || (str2[j]==a && str1[i]==z) || (str1[i]+1) == str2[j]) {
                j++;
            }
            i++;
        }
        return j == s2;
    }
};
