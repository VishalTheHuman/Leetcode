class Solution {
    public String sortSentence(String s) {
        String[] ret = s.split(" ");
        StringBuilder out = new StringBuilder();
        String[] ret1 = new String[ret.length];
        int[] index = new int[ret.length];
        for(int i=0;i<ret.length;i++){
            index[i]= ret[i].charAt(ret[i].length()-1)-'1';;
            ret1[index[i]]=ret[i].substring(0,ret[i].length()-1) + " ";
        }
        for(int i = 0;i<ret.length;i++){
            out.append(ret1[i]);
        }
        return out.toString().trim();
    }
}