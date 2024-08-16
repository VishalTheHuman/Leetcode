class Solution {
    public int numberOfBeams(String[] bank) {
        int count = 0;
        int current = 0;
        int prev = 0;
        for(String str:bank){
            current  = 0;
            for(char ch:str.toCharArray()){
                current+=(ch-'0');
            }
            if(current>0){
                count+= (current * prev);
                prev = current;
            }
        }
        return count;
    }
}