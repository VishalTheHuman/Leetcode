class Solution {
public:
    bool canAliceWin(int n) {
        bool turn = true; // True - Alice Wins; False - Bob Wins
        int current = 10; 
        while(true){
            if (n>=current){
                n-=current;
            }else{
                return !turn;
            }
            current--;
            turn = !turn; 
        }
        return false; 
    }
};
