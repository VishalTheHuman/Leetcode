class Solution {
    public String destCity(List<List<String>> paths) {
        HashMap<String,String> CD = new HashMap<>();
        for(List<String> tes:paths){
            if(CD.get(tes.get(0))==null){
                CD.put(tes.get(0),tes.get(1));
            }
        }
        for(List<String> tes:paths){
            if(CD.get(tes.get(1))==null){
                return tes.get(1);
            }
        }
        return "None";
    }
}