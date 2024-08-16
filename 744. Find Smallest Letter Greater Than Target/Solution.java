class Solution {
    public char nextGreatestLetter(char[] letters, char target) {
        for(char x : letters){
            if(Character.compare(x,target)>0){
                return x;
            }
        }
        return letters[0];
    }
}