class Solution {
    public int countConsistentStrings(String allowed, String[] words) {
        int count = 0;
        boolean flag = true;
        for(String x : words){
            flag = true;
            for(char y : x.toCharArray()){
                if(!allowed.contains(String.valueOf(y))){
                    flag=false;
                    break;
                }
            }
            if(flag){
                count+=1;
            }
        }
        return count;
    }
}