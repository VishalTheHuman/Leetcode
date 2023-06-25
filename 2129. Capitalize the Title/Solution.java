class Solution {
    public String capitalizeTitle(String s) {
        s = s.toLowerCase();
        String[] str = s.split(" ");
        StringBuilder ret = new StringBuilder();
        for(String title : str){
            if(title.length()>2){
                title = Character.toUpperCase(title.charAt(0)) + title.substring(1);
                ret.append(title);
                ret.append(" ");
            }else{
                ret.append(title);
                ret.append(" ");
            }
        }
        return ret.toString().trim();
    }
}