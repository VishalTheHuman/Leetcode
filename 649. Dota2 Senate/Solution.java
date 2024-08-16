class Solution {
    public String predictPartyVictory(String senate) {
        Queue<Character> queue = new LinkedList<>();
        int r = 0, d = 0;
        for(char x : senate.toCharArray()){
            if(x=='R'){
                r++;
            }else{
                d++;
            }
            queue.add(x);
        }
        int removeR = 0;
        int removeD = 0;
        while (queue.size()>1 && r!=0 && d!=0){
            char senator = queue.remove();
            if ((senator=='D' && removeD==0) || (senator=='R' && removeR==0)){
                queue.add(senator);
                if(senator=='D'){
                    removeR++;
                }else{
                    removeD++;
                }
            }else{
                if(senator=='D'){
                    removeD--;
                    d--;
                }else{
                    removeR--;
                    r--;
                }
            }
        }
        return r!=0 ? "Radiant" : "Dire";
    }
}