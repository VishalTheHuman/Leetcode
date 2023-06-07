class Solution {
    public int numUniqueEmails(String[] emails) {
        HashSet<String> ret = new HashSet<>();
        StringBuilder str = new StringBuilder();
        for(int i=0;i<emails.length;i++){
            str.setLength(0);
            int indexAt = emails[i].indexOf("@");
            String tes = emails[i].substring(0,indexAt).replace(".","");
            String dom = emails[i].substring(indexAt);
            if(tes.indexOf("+")!=-1){
                tes = tes.substring(0,tes.indexOf("+"));
            }
            str.append(tes);
            str.append(dom);
            ret.add(str.toString());
        }
        return ret.size();
    }
}