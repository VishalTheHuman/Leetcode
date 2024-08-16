class Solution {
    public int[] distributeCandies(int candies, int num_people) {
        int[] ret = new int[num_people];
        int i =0;
        int j=1;
        while(candies>0){
            if(candies>=j){
                ret[i]+=j;
                candies-=j;
            }else{
                ret[i]+=candies;
                candies=0;
            }
            i+=1;
            if(i==num_people) i=0;
            j+=1;
        }
        return ret;
    }
}