class Solution {
    public String[] sortPeople(String[] names, int[] heights) {
        Map<Integer,String> ret = new HashMap<>();
        int i=0;
        for(i=0;i<names.length;i++){
            ret.put(heights[i],names[i]);
        }
        Arrays.sort(heights);
        for(i=names.length-1;i>=0;i--){
            names[names.length-1-i] = ret.get(heights[i]);
        }
        return names;
    }
}