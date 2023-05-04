class Solution {
    public String predictPartyVictory(String senate) {
        int R_ind = 0;
        int D_ind = 0;
        int i = 0;
        while(i<senate.length()){
            if(senate.charAt(i)=='R'){
                if(D_ind>0){
                    D_ind--;
                }else{
                    R_ind++;
                    D_ind--;
                }
            }
            else if(senate.charAt(i)=='D'){
                if(R_ind>0){
                    R_ind--;
                }else{
                    D_ind++;
                    R_ind--;
                }
            }
            i++;
        }
        if(R_ind>D_ind){
            return "Radiant";
        }else{
            return "Dire";
        }
    }
}

public class Dota2Senate{
    public static void main(String[] args) {
        Solution obj = new Solution();
        System.out.println(obj.predictPartyVictory("RRDDD"));
    }
}