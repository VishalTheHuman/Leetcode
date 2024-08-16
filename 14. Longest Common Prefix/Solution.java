class Solution {
    public String longestCommonPrefix(String[] strs) {
        StringBuilder ret = new StringBuilder();
        boolean flag = true;
        for(int i = 0;i<strs[0].length();i++){
            for(int j =1;j<strs.length;j++){
                if(i<strs[j].length()){
                    if(strs[j].charAt(i)!=strs[0].charAt(i)){
                        flag = false;
                        break;
                    }
                }else{
                    flag = false;
                    break;
                }
            }
            if(flag == false){
                break;
            }else{
                ret.append(strs[0].charAt(i));
            }
        }
        return ret.toString();
    }
}