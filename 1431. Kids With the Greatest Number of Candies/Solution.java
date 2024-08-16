class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        ArrayList<Boolean> res = new ArrayList<Boolean>();
        int largest = candies[0];
        for(int i=1;i<candies.length;i++){
            if(candies[i]>largest){
                largest = candies[i];
            }
        }
        for(int i=0;i<candies.length;i++){
            if(candies[i]+extraCandies>=largest){
                res.add(true);
            }else{
                res.add(false);
            }
        }
        return res;
    }
}