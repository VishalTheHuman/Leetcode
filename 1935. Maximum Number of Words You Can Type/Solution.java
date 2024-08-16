class Solution {
    public int canBeTypedWords(String text, String brokenLetters) {
        int count = 0;
        boolean flag = true;
        String[] ret = text.split(" ");
        char[] arr = brokenLetters.toCharArray();
        for(String x : ret){
            flag = true;
            for(char y : arr){
                if(x.indexOf(y)!=-1 && flag){
                    flag = false;
                }
            }
            if(flag){
                count+=1;
            }
        }
        return count;
    }
}