class Solution {
    public int maximumValue(String[] strs) {
        int large;
        if(isInt(strs[0])){
            large = Integer.parseInt(strs[0]);
        }else{
            large = strs[0].length();
        }
        for(String str: strs){
            if(isInt(str)){
                if(Integer.parseInt(str)>large){
                    large = Integer.parseInt(str);
                }
            }else{
                if(str.length()>large){
                    large = str.length();
                }
            }
        }
        return large;
    }
    public boolean isInt(String str){
        try{
            Integer.parseInt(str);
            return true;
        }catch(NumberFormatException e){
            return false;
        }
    }
}