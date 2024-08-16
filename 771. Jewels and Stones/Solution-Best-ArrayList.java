class Solution {
    public int numJewelsInStones(String jewels, String stones) {
        List<Character> jewel = new ArrayList<>();
        for(char x : jewels.toCharArray()){
            if(jewel.indexOf(x)==-1){
                jewel.add(x);
            }
        }
        int count = 0;
        for(char x: stones.toCharArray()){
            if(jewel.indexOf(x)!=-1){
                count+=1;
            }
        }
        return count;
    }
}