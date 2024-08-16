class Solution {
    public int countSeniors(String[] details) {
        int count = 0;
        for(String x : details){
            if(Integer.parseInt(x.substring(11,13))>60){
                count+=1;
            }
        }
        return count;
    }
}