class Solution {
    public String sortSentence(String s) {
        String[] ret = s.split(" ");
        StringBuilder out = new StringBuilder();
        String[] ret1 = new String[ret.length];
        for(int i=0;i<ret.length;i++){
            ret1[ret[i].charAt(ret[i].length()-1)-'1']=ret[i].substring(0,ret[i].length()-1) + " ";
        }
        for(int i = 0;i<ret.length;i++){
            out.append(ret1[i]);
        }
        return out.toString().trim();
    }
}