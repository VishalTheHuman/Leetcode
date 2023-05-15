class Solution {
    public int countMatches(List<List<String>> items, String ruleKey, String ruleValue) {
        int checkInd,count =0;
        if(ruleKey.equals("type")){
            checkInd = 0;
        }else if(ruleKey.equals("color")){
            checkInd = 1;
        }else{
            checkInd = 2;
        }
        for(int i =0;i<items.size();i++){
            if((items.get(i).get(checkInd)).equals(ruleValue)){
                count++;
            }
        }
        return count;
    }
}