class Solution {
    public int numJewelsInStones(String jewels, String stones) {
        HashSet<Character> jewel = new HashSet<>();
        for(char x : jewels.toCharArray()){
            jewel.add(x);
        }
        int count = 0;
        for(char x: stones.toCharArray()){
            if(jewel.contains(x)){
                count+=1;
            }
        }
        return count;
    }
}